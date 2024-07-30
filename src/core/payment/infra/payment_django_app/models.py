from django.db import models

from core.__seedwork.infra.django.models import BaseModelWithTenantAndHistory
from core.tenant.infra.tenant_django_app.models import Tenant, Reservation, Vehicle, Client

class PaymentMethods(BaseModelWithTenantAndHistory):
    description  = models.CharField(max_length=255)

    class Meta:
        db_table: str = "payment_methods"
        verbose_name: str = "Payment Method"
        verbose_name_plural: str = "Payment Methods"
        ordering: list[str] = ["-created_at"]

    def __str__(self):
        return self.description


class CreditCard(BaseModelWithTenantAndHistory):
    card_number = models.CharField(max_length=16)
    expiration_date = models.DateField()
    cvv = models.CharField(max_length=3)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)

    class Meta:
        db_table: str = "credit_card"
        verbose_name: str = "Credit Card"
        verbose_name_plural: str = "Credit Cards"
        ordering: list[str] = ["-created_at"]

    def __str__(self):
        return f"{self.card_number}, {self.expiration_date}, {self.is_active}"


class Payment(BaseModelWithTenantAndHistory):
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.PROTECT,    
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT, 
    )
    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.PROTECT,
        
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,   
    )
    payment_method = models.ForeignKey(
        PaymentMethods,
        on_delete=models.PROTECT,
        
    )
    card_data = models.ForeignKey(
        CreditCard,
        on_delete=models.PROTECT,
        
    )
    payment_date = models.DateTimeField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table: str = "payment"
        verbose_name: str = "Payment"
        verbose_name_plural: str = "Payments"
        ordering: list[str] = ["-created_at"]

    def __str__(self):
        return f"{self.tenant}, {self.payment_amount}, {self.client}"

