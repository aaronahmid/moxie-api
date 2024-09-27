from rest_framework import serializers
from core.models import MedSpa, Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class MedSpaSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedSpa
        fields = "__all__"
