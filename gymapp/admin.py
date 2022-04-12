from django.contrib import admin
from .models import Couches, PriceList, SportStyle
from .models import Contact

admin.site.register(Couches)
admin.site.register(PriceList)
admin.site.register(SportStyle)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass