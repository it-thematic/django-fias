
from django.contrib import admin
from django.forms import forms
from django_select2.forms import Select2Widget

from tst.models import *


class ItemAdmin(admin.ModelAdmin):
    class Media:
        js = ['//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js']

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemWithArea, ItemAdmin)

admin.site.register(CachedAddress, ItemAdmin)
# admin.site.register(CachedAddressWithArea, ItemAdmin)
admin.site.register(CachedAddressWithHouse, ItemAdmin)
#admin.site.register(NullableAddressItem, ItemAdmin)
