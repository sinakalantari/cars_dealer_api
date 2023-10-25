from rest_framework.exceptions import ValidationError

from .models import CarsName, CarsModel, CarsBrand, CarsColor, CarsInventory, Location, CarType
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class CarTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model= CarType
        fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsColor
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsBrand
        fields = "__all__"


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsModel
        fields = "__all__"


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsName
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsInventory
        fields = '__all__'
        extra_kwargs = {'color': {'required': True, 'allow_null': False},
                        'brand': {'required': True, 'allow_null': False},
                        'model': {'required': True, 'allow_null': False},
                        'name': {'required': True, 'allow_null': False}}

    def create(self, validated_data):
        brand = validated_data.pop('brand')
        model = validated_data.pop('model')
        name = validated_data.pop('name')
        color = validated_data.pop('color')
        if name.model_id == model.id and model.brand_id == brand.id:
            car = CarsInventory.objects.create(**validated_data, brand=brand, model=model, name=name, color=color)
            return car
        raise ValidationError('مقادیر وارد شده همخوانی ندارند!')
