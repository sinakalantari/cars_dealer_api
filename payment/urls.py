from django.urls import path
from .views import PaymentView, PaymentTypeView, AvailableContractView


urlpatterns = [
    path('create', PaymentView.as_view(), name='payment_create'),
    path('type', PaymentTypeView.as_view(), name='payment_type'),
    path('available-contract', AvailableContractView.as_view(), name='available_contract'),

]