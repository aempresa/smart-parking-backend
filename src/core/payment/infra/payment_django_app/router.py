from rest_framework.routers import DefaultRouter

from core.payment.infra.payment_django_app.views import PaymentViewSet, PaymentMethodsViewSet, CreditCardViewSet

router = DefaultRouter()
router.register(r'credit-cards', CreditCardViewSet, basename='credit-cards')
router.register(r'payment-methods', PaymentMethodsViewSet, basename='payment-methods')
router.register(r'payment', PaymentViewSet, basename='payment')
