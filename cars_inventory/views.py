from .models import CarsModel, CarsName, CarsBrand, CarsInventory, CarsColor, Location, CarType
from rest_framework import generics
from .serializers import InventorySerializer, BrandSerializer, ModelSerializer, NameSerializer, ColorSerializer, \
    LocationSerializer, CarTypeSerializer
from rest_framework.response import Response
from rest_framework import status
from misc.custom_permission import IsSupervisor, IsManagement


class LocationInventoryView(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    permission_classes = (IsManagement,)


class LocationInventoryEdit(generics.RetrieveUpdateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class CarTypeInventoryView(generics.ListCreateAPIView):
    serializer_class = CarTypeSerializer
    queryset = CarType.objects.all()


class CarTypeInventoryEdit(generics.RetrieveUpdateAPIView):
    serializer_class = CarTypeSerializer
    queryset = CarType.objects.all()


class ColorInventoryView(generics.ListCreateAPIView):
    serializer_class = ColorSerializer
    queryset = CarsColor.objects.all()
    permission_classes = (IsSupervisor,)


class ColorInventoryEdit(generics.RetrieveUpdateAPIView):
    serializer_class = ColorSerializer
    queryset = CarsColor.objects.all()


class BrandInventoryView(generics.ListCreateAPIView):
    serializer_class = BrandSerializer
    queryset = CarsBrand.objects.all()


class BrandInventoryEdit(generics.RetrieveUpdateAPIView):
    serializer_class = BrandSerializer
    queryset = CarsBrand.objects.all()


class ModelInventoryView(generics.ListCreateAPIView):
    serializer_class = ModelSerializer
    queryset = CarsModel.objects.all()

    def get(self, request, *args, **kwargs):
        model = CarsModel.objects.filter(brand_id=self.kwargs.get('pk'))
        serializer = ModelSerializer(model, many=True)
        if len(model) == 0:
            return Response(status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ModelInventoryEdit(generics.RetrieveUpdateAPIView):
    serializer_class = ModelSerializer
    queryset = CarsModel.objects.all()


class NameInventoryView(generics.ListCreateAPIView):
    serializer_class = NameSerializer
    queryset = CarsName.objects.all()

    def get(self, request, *args, **kwargs):
        model = CarsName.objects.filter(model_id=self.kwargs.get('pk'))
        serializer = NameSerializer(model, many=True)
        if len(model) == 0:
            return Response(status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NameInventoryEdit(generics.RetrieveUpdateAPIView):
    serializer_class = NameSerializer
    queryset = CarsName.objects.all()


class InventoryView(generics.CreateAPIView):
    serializer_class = InventorySerializer


class InventoryEdit(generics.RetrieveUpdateAPIView):
    serializer_class = InventorySerializer
    queryset = CarsInventory.objects.all()
