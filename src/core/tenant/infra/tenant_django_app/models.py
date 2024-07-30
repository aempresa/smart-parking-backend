from django.db import models

from core.__seedwork.infra.django.models import BaseModelWithTenantAndHistory, BaseModelWithHistory
from core.user.infra.user_django_app.models import User

class Tenant(BaseModelWithHistory):
    name = models.CharField(max_length=255)
    corporate_name = models.CharField(max_length=255)
    fantasy_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cnpj = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    car_spaces = models.IntegerField()
    motorcycle_spaces = models.IntegerField()
    # photo = models.ImageField(upload_to="tenants", null=True, blank=True)
    have_car_wash = models.BooleanField(default=False)
    is_24_hours = models.BooleanField(default=False)
    is_covered = models.BooleanField(default=False)
    is_open = models.BooleanField(default=False)
    security_guard = models.BooleanField(default=False)
    camera = models.BooleanField(default=False)



    def __str__(self):
        return self.name

    class Meta:
        db_table: str = "tenant"
        verbose_name: str = "Tenant"
        verbose_name_plural: str = "Tenants"
        ordering: list[str] = ["-created_at"]

class Client(BaseModelWithTenantAndHistory):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="clients",
        blank = True,
        null = True
    )
    cpf = models.CharField(max_length=11, blank=True, null=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    # pic = faz essa bomba rafa


class Vehicle(BaseModelWithTenantAndHistory):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
    )
    plate = models.CharField(max_length=7)
    model = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    year = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.plate

    class Meta:
        db_table: str = "vehicle"
        verbose_name: str = "Vehicle"
        verbose_name_plural: str = "Vehicles"
        ordering: list[str] = ["-created_at"]

class Reservation(BaseModelWithTenantAndHistory):
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name= "reservations_vehicle"
    )
    parking = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name= "reservations_parking"
    )
    pre_exit = models.DateTimeField(blank=True, null=True)
    pre_entry = models.DateTimeField(blank=True, null=True)
    entry = models.DateTimeField()
    exit = models.DateTimeField()
    value = models.FloatField()
    is_active = models.BooleanField(default=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.vehicle} - {self.parking}"
    
    class Meta:
        db_table: str = "reservation"
        verbose_name: str = "Reservation"
        verbose_name_plural: str = "Reservations"
        ordering: list[str] = ["-created_at"]