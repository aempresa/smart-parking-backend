from rest_framework.routers import DefaultRouter
from core.user.infra.user_django_app.router import router as user_router

router = DefaultRouter()
router.registry.extend(user_router.registry)