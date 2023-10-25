from django.urls import path
from .views import (BrandInventoryView, ModelInventoryView, NameInventoryView, InventoryView,
                    ColorInventoryView, CarTypeInventoryView, LocationInventoryView, LocationInventoryEdit,
                    CarTypeInventoryEdit, ColorInventoryEdit, BrandInventoryEdit, ModelInventoryEdit,
                    NameInventoryEdit, InventoryEdit)



urlpatterns = [
    path('cars-brand', BrandInventoryView.as_view(), name='cars_brand'),
    path('cars-brand/<int:pk>', BrandInventoryEdit.as_view(), name='cars_brand_edit'),
    path('cars-model/<int:pk>', ModelInventoryView.as_view(), name='cars_model'),
    path('cars-model/edit/<int:pk>', ModelInventoryEdit.as_view(), name='cars_model_edit'),
    path('cars-name/<int:pk>', NameInventoryView.as_view(), name='cars_name'),
    path('cars-name/edit/<int:pk>', NameInventoryEdit.as_view(), name='cars_name_edit'),
    path('cars-inventory', InventoryView.as_view(), name='cars_inventory'),
    path('cars-inventory/<int:pk>', InventoryEdit.as_view(), name='cars_inventory_edit'),
    path('cars-color', ColorInventoryView.as_view(), name='cars_color'),
    path('cars-color/<int:pk>', ColorInventoryEdit.as_view(), name='cars_color_edit'),
    path('cars-location', LocationInventoryView.as_view(), name='cars_location'),
    path('cars-location/<int:pk>', LocationInventoryEdit.as_view(), name='cars_location_edit'),
    path('cars-type', CarTypeInventoryView.as_view(), name='cars_type'),
    path('cars-type/<int:pk>', CarTypeInventoryEdit.as_view(), name='cars_type_edit'),


]
