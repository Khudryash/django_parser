from django.db import models


# Модель таблицы "Закупки"
class Purcase(models.Model):
    number = models.CharField(max_length=100, verbose_name="Номер", unique=True, db_index=True)
    start_price = models.FloatField(verbose_name="Стартовая цена", null=True)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name_plural = "Закупки"
        verbose_name = "Закупка"
        ordering = ['-number']


# Модель таблицы "Данные"
class Values(models.Model):
    purchase = models.OneToOneField(Purcase, on_delete=models.CASCADE, verbose_name="Закупка")
    calculation = models.FloatField(verbose_name="Расчёт", null=True)

    def __str__(self):
        return str(self.calculation)

    class Meta:
        verbose_name_plural = "Данные"
        verbose_name = "Данные"
