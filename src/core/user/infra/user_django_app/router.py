from rest_framework.routers import DefaultRouter

from core.user.infra.user_django_app.views import UserViewSet


router = DefaultRouter()
router.register("user", UserViewSet)
