from rest_framework import generics
from .serializers import PositionSerializer, UserProfileSerializer, UserProfileClientSerializer
from .models import UserProfileModel, PositionsModel
from misc.custom_permission import IsOwner


class PositionView(generics.ListCreateAPIView):
    serializer_class = PositionSerializer
    queryset = PositionsModel.objects.all()


class PositionEdit(generics.RetrieveUpdateAPIView):
    serializer_class = PositionSerializer
    queryset = PositionsModel.objects.all()


class UserProfileView(generics.CreateAPIView):
    serializer_class = UserProfileSerializer


class UserProfileEdit(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfileModel.objects.all()


class UserProfileClient(generics.RetrieveAPIView):
    serializer_class = UserProfileClientSerializer
    queryset = UserProfileModel.objects.all()
    permission_classes = (IsOwner,)