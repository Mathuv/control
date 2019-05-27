from rest_framework import serializers as drf_serializers
from rest_framework_json_api import serializers


class PulseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
