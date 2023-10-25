from rest_framework import generics
from .models import SaleContract, LeasingNameModel, SaleMethodModel
from .serializers import SaleContractSerializer, LeasingNameSerializer, SaleMethodSerializer
from cars_inventory.serializers import InventorySerializer
from cars_inventory.models import CarsInventory


class SaleContractView(generics.CreateAPIView):
    serializer_class = SaleContractSerializer


class LeasingNameView(generics.ListCreateAPIView):
    serializer_class = LeasingNameSerializer
    queryset = LeasingNameModel.objects.filter(active=True)


class SaleMethodView(generics.ListCreateAPIView):
    serializer_class = SaleMethodSerializer
    queryset = SaleMethodModel.objects.filter(active=True)


class SaleMethodEdit(generics.RetrieveUpdateAPIView):
    serializer_class = SaleMethodSerializer
    queryset = SaleMethodModel.objects.all()


class ChassisView(generics.ListAPIView):
    serializer_class = InventorySerializer
    queryset = CarsInventory.objects.exclude(
        chassis_num__in=SaleContract.objects.all().values_list('chassisnum__chassis_num'))
