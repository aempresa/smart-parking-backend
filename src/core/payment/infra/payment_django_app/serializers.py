from rest_framework import serializers
from core.payment.infra.payment_django_app.models import Payment, PaymentMethods, CreditCard

class PaymentMethodsRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethods
        fields: list[str] = [
            "id",
            "description",
            "created_at",
            "updated_at",
            "deleted_at",
        ]

class PaymentMethodsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethods
        fields: list[str] = [
            "id",
            "description",
        ]

class PaymentMethodsWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethods
        fields: list[str] = [
            "description",
        ]

class CreditCardRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields: list[str] = [
            "id",
            "card_number",
            "expiration_date",
            "cvv",
            "is_active",
            "is_default",
            "created_at",
            "updated_at",
            "deleted_at",
        ]

class CreditCardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields: list[str] = [
            "id",
            "card_number",
            "expiration_date",
            "cvv",
            "is_active",
            "is_default",
        ]

class CreditCardWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields: list[str] = [
            "card_number",
            "expiration_date",
            "cvv",
            "is_active",
            "is_default",
        ]

class PaymentRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields: list[str] = [
            "id",
            "tenant",
            "client",
            "reservation",
            "vehicle",
            "payment_method",
            "card_data",
            "payment_date",
            "created_at",
            "updated_at",
            "deleted_at",
        ]

class PaymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields: list[str] = [
            "id",
            "tenant",
            "client",
            "reservation",
            "vehicle",
            "payment_method",
            "card_data",
            "payment_date",
        ]

class PaymentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields: list[str] = [
            "tenant",
            "client",
            "reservation",
            "vehicle",
            "payment_method",
            "card_data",
            "payment_date",
        ]

