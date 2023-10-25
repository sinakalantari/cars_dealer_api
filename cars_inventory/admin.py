from django.contrib import admin
from .models import CarsBrand, CarsInventory, CarsName, CarsModel, CarsColor, StatusModel

# Register your models here.

admin.site.register(CarsBrand)
admin.site.register(CarsInventory)
admin.site.register(CarsModel)
admin.site.register(CarsColor)
admin.site.register(CarsName)
admin.site.register(StatusModel)
