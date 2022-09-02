from rest_framework import serializers
from .models import Tarjetas

class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjetas
        fields = "__all__"
        read_only_fields = (
            "customer_id",
        )