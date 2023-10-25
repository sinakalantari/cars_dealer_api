from django.urls import path
from .views import CarDeliverView, DeliverExpertsView, CarDeliverEdit

urlpatterns = [
    path('create', CarDeliverView.as_view(), name='car_deliver'),
    path('<int:pk>', CarDeliverEdit.as_view(), name='car_deliver_edit'),
    path('deliver-expert',DeliverExpertsView.as_view(), name='deliver_expert')

]
