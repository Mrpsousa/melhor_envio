from rest_framework import serializers
from .models import Consumer, Service


class ConsumerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consumer
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = "__all__"
