from rest_framework import serializers
from .models import PaymentModel, PaymentTypeModel


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTypeModel
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = '__all__'
        extra_kwargs = {
            'payment_image': {'write_only': True}
        }
