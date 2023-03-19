import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from main.models import Purcase, Values


class PageParser:
    headers = {
        'Accept': '*/*',
        'User-Agent': UserAgent().random
    }
    url = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?morphology=on&search-filter' \
          '=Дате+размещения&pageNumber={page}&sortDirection=false&recordsPerPage=_200&showLotsInfoHidden=false' \
          '&sortBy=UPDATE_DATE&fz44=on&fz223=on&currencyIdGeneral=-1'

    html_content = None
    soup = None

    # Получение данных со страницы
    def get_page_value(self, page):

        self.html_content = requests.get(url=self.url.format(page=page), headers=self.headers)

        self.soup = BeautifulSoup(self.html_content.text, 'lxml')
        scope = self.soup.find_all(class_='registry-entry__form')

        for item in scope:

            num = item \
                .find(class_='registry-entry__header-mid__number') \
                .find('a') \
                .text \
                .replace(u'\xa0', '') \
                .replace('№', '').strip()
            price = item \
                .find(class_='price-block__value')

            # Запись в бд с предварительной проверкой на наличие значения
            if price is not None:
                price = price \
                    .text \
                    .replace(' ', '') \
                    .replace(u'\xa0', '')[:-2] \
                    .replace(',', '.')

                obj = Purcase.objects.update_or_create(number=num, start_price=float(price))
                Values.objects.update_or_create(purchase=obj[0], calculation=round(float(price) * 10, 1))
            else:
                obj = Purcase.objects.update_or_create(number=num, start_price=None)
                Values.objects.update_or_create(purchase=obj[0], calculation=None)

    # Получение номера последней страницы
    def get_page_count(self):
        return int(self.soup.find_all(class_='page')[-1].find('span').text.strip())
