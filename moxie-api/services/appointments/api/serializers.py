from rest_framework import serializers
from core.models import MedSpa


class MedSpaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedSpa
        fields = "__all__"
