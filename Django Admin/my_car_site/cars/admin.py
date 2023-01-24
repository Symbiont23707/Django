from django.contrib import admin
from cars.models import Cars

# Register your models here.

class CarsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Time Information',{'fields':['year']}),
        ('Car Information',{'fields':['brand']})
    ]

admin.site.register(Cars,CarsAdmin)