from django.contrib.auth.models import User
from rest_framework import serializers
from .models import PositionsModel, UserProfileModel


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionsModel
        fields = "__all__"


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email']


class UserProfileSerializer(serializers.ModelSerializer):
    # user = UserSerializer(write_only=True)

    class Meta:
        model = UserProfileModel
        fields = '__all__'

    # def create(self, validated_data):
    #     user = validated_data.pop('user')
    #     my_user = User.objects.create_user(**user)
    #     profile = UserProfileModel.objects.create(**validated_data, user=my_user)
    #     return 200


class UserProfileClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = '__all__'
