from rest_framework.viewsets import ModelViewSet
from core.tenant.infra.tenant_django_app.models import Tenant, Vehicle, Client, Reservation
from core.tenant.infra.tenant_django_app.serializers import ClientRetriveSerializer, ClientListSerializer, ClientWriteSerializer, VehicleRetriveSerializer, VehicleListSerializer, VehicleWriteSerializer, ReservationRetriveSerializer, ReservationListSerializer, ReservationWriteSerializer, TenantRetriveSerializer, TenantListSerializer, TenantWriteSerializer

from core.tenant.infra.tenant_django_app.models import Tenant, Vehicle, Client, Reservation


class TenantViewSet(ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantRetriveSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return TenantListSerializer
        if self.action == "create" or self.action == "update":
            return TenantWriteSerializer
        return TenantRetriveSerializer
    

class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleRetriveSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return VehicleListSerializer
        if self.action == "create" or self.action == "update":
            return VehicleWriteSerializer
        return VehicleRetriveSerializer
    

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientRetriveSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ClientListSerializer
        if self.action == "create" or self.action == "update":
            return ClientWriteSerializer
        return ClientRetriveSerializer




class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationRetriveSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ReservationListSerializer
        if self.action == "create" or self.action == "update":
            return ReservationWriteSerializer
        return ReservationRetriveSerializer
    


class TenantViewSet(ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantRetriveSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return TenantListSerializer
        if self.action == "create" or self.action == "update":
            return TenantWriteSerializer
        return TenantRetriveSerializer
    

