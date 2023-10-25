from django.urls import path
from .views import CustomerView, CustomerEdit

urlpatterns = [
    path('', CustomerView.as_view(), name='customer'),
    path('edit/<int:pk>', CustomerEdit.as_view(), name='customer_edit'),

]
