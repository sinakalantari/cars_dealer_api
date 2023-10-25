from rest_framework import serializers
from .models import SaleContract, LeasingNameModel, SaleMethodModel


class SaleMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleMethodModel
        fields = "__all__"


class SaleContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleContract
        fields = "__all__"


class LeasingNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeasingNameModel
        fields = "__all__"
