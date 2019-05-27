from rest_framework import serializers as drf_serializers
from rest_framework_json_api import serializers
from .models import Pulse


class PulseSerializer(serializers.ModelSerializer):
    def validate_polar_angle(self, data):
        if data < 0 or data > 1:
            raise serializers.ValidationError(
                {
                    "detail": "Value should be between 0 and 1",
                    "source": {"pointer": "/data/attributes/polarAngle"},
                    "status": "400",
                }
            )
        return data

    def validate_max_rabi_rate(self, data):
        if data < 0 or data > 100:
            raise serializers.ValidationError(
                {
                    "detail": "Value should be between 0 and 100",
                    "source": {"pointer": "/data/attributes/maxRabiRate"},
                    "status": "400",
                }
            )
        return data

    class Meta:
        model = Pulse
        fields = "__all__"
        read_only_fields = ("id",)
