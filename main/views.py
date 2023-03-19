from django.shortcuts import render
import time
from .models import Purcase
from .pageparser import PageParser
import logging

logging.basicConfig(level=logging.DEBUG)


def home(response):
    if response.method == 'POST':
        start_time = time.time()

        parser = PageParser()
        parser.get_page_value(1)
        pages = parser.get_page_count()
        for i in range(2, pages + 1):
            parser.get_page_value(i)

        logging.info("--- %s seconds ---" % (time.time() - start_time))

    return render(response, 'main/home.html', {
        "number": 0,
        "calculation": 0
    })


def page(response, number):
    pur_obj = Purcase.objects \
        .select_related('values') \
        .only('number', 'values__calculation') \
        .filter(number=number).first()

    if pur_obj is not None:
        pur_number = pur_obj.number

        if pur_obj.values is not None:
            pur_calculation = str(pur_obj.values.calculation) + "₽"
        else:
            pur_calculation = 'Данные отсутствуют'
    else:
        pur_number = 'Данные отсутствуют'
        pur_calculation = 'Данные отсутствуют'

    return render(response, 'main/page.html', {
        "number": pur_number,
        "calculation": pur_calculation
    })


def load(response):
    return render(response, 'main/load.html', {})
