from rest_framework import generics
from .serializers import CustomerSerializer
from .models import CustomerModel


class CustomerView(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = CustomerModel.objects.all()


class CustomerEdit(generics.RetrieveUpdateAPIView):
    serializer_class = CustomerSerializer
    queryset = CustomerModel.objects.all()
