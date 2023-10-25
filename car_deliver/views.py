from rest_framework import generics
from .serializers import CarDeliverSerializer
from .models import CarDeliverModel
from cars_account.serializers import UserProfileSerializer
from cars_account.models import UserProfileModel


class CarDeliverView(generics.CreateAPIView):
    serializer_class = CarDeliverSerializer
    queryset = CarDeliverModel.objects.all()


class CarDeliverEdit(generics.RetrieveUpdateAPIView):
    serializer_class = CarDeliverSerializer
    queryset = CarDeliverModel.objects.all()


class DeliverExpertsView(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfileModel.objects.filter(buyacc=True)
