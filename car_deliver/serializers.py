from rest_framework import serializers
from .models import CarDeliverModel


class CarDeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDeliverModel
        fields = '__all__'
