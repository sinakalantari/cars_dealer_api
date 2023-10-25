from rest_framework import generics, status
from rest_framework.parsers import FileUploadParser, MultiPartParser
from sales_contract.models import SaleContract
from sales_contract.serializers import SaleContractSerializer

from .serializers import PaymentSerializer, PaymentTypeSerializer
from .models import PaymentTypeModel, PaymentModel


class PaymentTypeView(generics.ListCreateAPIView):
    serializer_class = PaymentTypeSerializer
    queryset = PaymentTypeModel.objects.filter(active=True)


class PaymentView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = PaymentModel.objects.all()
    parser_classes = (MultiPartParser,)


class AvailableContractView(generics.ListAPIView):
    serializer_class = SaleContractSerializer
    queryset = SaleContract.objects.filter(payment=False)