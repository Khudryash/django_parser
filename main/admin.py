from django.contrib import admin
from .models import Purcase, Values


class PurcAdmin(admin.ModelAdmin):
    list_display = ('number', 'start_price', 'id')
    list_display_links = ('number',)
    search_fields = ['number']
# admin.site.register(Purcase, PurcAdmin)


class PurcInline(admin.StackedInline):
    model = Values
    fields = ('purchase', 'calculation')


class ValAdmin(admin.ModelAdmin):
    list_display = ('purchase', 'calculation')
    list_display_links = ('purchase',)


class ExtendedPurchAdmin(PurcAdmin):
    inlines = PurcAdmin.inlines + [PurcInline]


admin.site.register(Purcase, ExtendedPurchAdmin)
admin.site.register(Values, ValAdmin)
# Register your models here.
