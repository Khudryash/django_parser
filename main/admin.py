from django.contrib import admin
from .models import Purcase, Values


# Настройка отображения таблицы "Закупка" в административной панели
class PurcAdmin(admin.ModelAdmin):
    list_display = ('number', 'start_price', 'id')
    list_display_links = ('number',)
    search_fields = ['number']


# Настройка инлайн-отображения связанной сущности таблицы "Данные"
class ValuesInline(admin.StackedInline):
    model = Values
    fields = ('purchase', 'calculation')


# Связка и отображение в даминистративной панели
class ExtendedPurchAdmin(PurcAdmin):
    inlines = PurcAdmin.inlines + [ValuesInline]


admin.site.register(Purcase, ExtendedPurchAdmin)

'''
Опциональна отдельное отображение таблицы "Данные"

class ValAdmin(admin.ModelAdmin):
    list_display = ('purchase', 'calculation')
    list_display_links = ('purchase',)
    

admin.site.register(Values, ValAdmin)
'''
