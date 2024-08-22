from rest_framework import serializers
from core.tenant.infra.tenant_django_app.models import Tenant, Vehicle, Client, Reservation


class ClientRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields: list[str] = ['id', 'name', 'email', 'phone', 'address', 'created_at', 'updated_at']



class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields: list[str] = ['id', 'name', 'email', 'phone', 'address']


class ClientWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields: list[str] = ['name', 'email', 'phone', 'address']

class VehicleRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields: list[str] = ['id', 'plate', 'model', 'brand', 'year', 'color', 'is_active', 'created_at', 'updated_at']


class VehicleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields: list[str] = ['id', 'plate', 'model', 'brand', 'year', 'color', 'is_active']


class VehicleWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields: list[str] = ['plate', 'model', 'brand', 'year', 'color', 'is_active']


class ReservationRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields: list[str] = ['id', 'client', 'vehicle', 'start_date', 'end_date', 'is_active', 'created_at', 'updated_at']

class ReservationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields: list[str] = ['id', 'client', 'vehicle', 'start_date', 'end_date', 'is_active']

class ReservationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields: list[str] = ['client', 'vehicle', 'start_date', 'end_date', 'is_active']

class TenantRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields: list[str] = ['id', 'name', 'email', 'phone', 'address', 'created_at', 'updated_at']


class TenantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields: list[str] = ['id', 'name', 'email', 'phone', 'address']


class TenantWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields: list[str] = ['name', 'email', 'phone', 'address']

