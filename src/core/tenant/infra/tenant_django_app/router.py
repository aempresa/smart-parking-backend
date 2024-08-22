from rest_framework.routers import DefaultRouter
from core.tenant.infra.tenant_django_app.views import TenantViewSet, VehicleViewSet, ClientViewSet, ReservationViewSet

router = DefaultRouter()

router.register(r'tenant', TenantViewSet, basename='tenant')
router.register(r'vehicle', VehicleViewSet, basename='vehicle')
router.register(r'client', ClientViewSet, basename='client')
router.register(r'reservation', ReservationViewSet, basename='reservation')
