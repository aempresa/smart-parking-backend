from rest_framework.routers import DefaultRouter
from core.user.infra.user_django_app.router import router as user_router
from core.payment.infra.payment_django_app.router import router as payment_router
from core.tenant.infra.tenant_django_app.router import router as tenant_router

router = DefaultRouter()
router.registry.extend(user_router.registry)
router.registry.extend(payment_router.registry)
router.registry.extend(tenant_router.registry)
