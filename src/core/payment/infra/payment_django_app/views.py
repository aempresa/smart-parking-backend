from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from core.payment.infra.payment_django_app.models import Payment, PaymentMethods, CreditCard
from core.payment.infra.payment_django_app.serializers import PaymentMethodsRetriveSerializer, PaymentMethodsListSerializer, PaymentMethodsWriteSerializer, CreditCardRetriveSerializer, CreditCardListSerializer, CreditCardWriteSerializer, PaymentRetriveSerializer, PaymentListSerializer, PaymentWriteSerializer


class PaymentMethodsViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethods.objects.all()
    serializer_class = PaymentMethodsRetriveSerializer
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "list":
            return PaymentMethodsListSerializer
        if self.action == "create" or self.action == "update":
            return PaymentMethodsWriteSerializer
        return PaymentMethodsRetriveSerializer
    
class CreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardRetriveSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    

    def get_serializer_class(self):
        if self.action == "list":
            return CreditCardListSerializer
        if self.action == "create" or self.action == "update":
            return CreditCardWriteSerializer
        return CreditCardRetriveSerializer
    

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentRetriveSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    
    
    def get_queryset_class (self):
        if self.action == "list":
            return PaymentListSerializer
        if self.action == "create" or self.action == "update":
            return PaymentWriteSerializer
        return PaymentRetriveSerializer
