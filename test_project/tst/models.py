from django.db import models

# Create your models here.

from fias.fields import AddressField, ChainedAreaField
from fias.models import AddrObj, FIASAddress, FIASAddressWithArea, FIASHouse


class Item(models.Model):
    title = models.CharField('title', max_length=100)
    location_id = AddressField(db_column='location_id')


class ItemWithArea(models.Model):

    title = models.CharField('title', max_length=100)
    location = AddressField()
    area = ChainedAreaField(AddrObj, address_field='location', related_name='+')


class CachedAddress(FIASAddress):
   pass

class CachedAddressWithHouse(FIASAddress, FIASHouse):
    pass

#class CachedAddressWithArea(FIASAddressWithArea):
#    pass


#class CachedAddressWithHouse(FIASAddress, FIASHouse):
#    pass

#class NullableAddressItem(models.Model):
#    title = models.CharField('title', max_length=100)
#
#    location = AddressField(blank=True, null=True)
