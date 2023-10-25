from django.urls import path

from .views import SaleContractView, ChassisView, LeasingNameView, SaleMethodView, SaleMethodEdit

urlpatterns = [
    path('contract', SaleContractView.as_view(), name='sale_contract'),
    path('available-chassis', ChassisView.as_view(), name='available_chassis'),
    path('leasingname', LeasingNameView.as_view(), name='leasing_name'),
    path('salemethod', SaleMethodView.as_view(), name='sale_method'),
    path('salemethod/<int:pk>', SaleMethodEdit.as_view(), name='sale_method_edit'),
]
