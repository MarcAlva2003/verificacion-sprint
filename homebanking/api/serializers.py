from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from Clientes.models import clientes
from sucursales.models import Sucursal
from prestamos.models import prestamos as Prestamos
from Cuentas.models import cuenta

class BalanceCuentaSerializer(serializers.Serializer):
    tipo_de_cuenta=serializers.CharField(max_length=20)
    iban=serializers.CharField(max_length=24)
    balance=serializers.IntegerField()

class AllDataBalanceCuentaSerializer(serializers.Serializer):
    iban=serializers.CharField(max_length=24)
    tipo_de_cuenta=serializers.CharField(max_length=20)
    balance=serializers.IntegerField(default=0)
    customer_id=serializers.IntegerField()
    user_email=serializers.EmailField(max_length=254)

class ClienteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = clientes
        fields = "__all__"
        read_only_fields = (
            "name",
            "surname",
            "dni",
            "tipo_cliente",
            "created_at",
            "updated_at",
            "account_id",
            "owner",
        )

class UserSerializer(serializers.ModelSerializer):
    clientes = serializers.PrimaryKeyRelatedField(many=True, queryset=clientes.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'clientes']



class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"
        read_only_fields = (
        "id",
        "created_at",
        "updated_at",
        )

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Prestamos
        #indicamos que use todos los campos 
        fields = "__all__" 
        # #les decimos cuales son los de solo lectura 
        read_only_fields = ( 
            "id",
            "id_cliente",
            "created_at",
        )

class MontoPrestamosDeClienteSerializer(serializers.Serializer):
    loan_total = serializers.FloatField()

class MontoPrestamosSucursalSerializer(serializers.Serializer):
    loan_total = serializers.FloatField()