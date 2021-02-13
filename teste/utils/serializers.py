from rest_framework import serializers
from ..models import WorkData


class WorkDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkData
        fields = "__all__"

