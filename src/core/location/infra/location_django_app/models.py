from django.db import models

from core.__seedwork.infra.django.models import BaseModel


class State(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    initials = models.CharField(max_length=2, null=False, blank=False)
    ibge_code = models.CharField(
        max_length=10, null=False, blank=False, unique=True, db_index=True
    )

    class Meta:
        db_table: str = "state"

    def __str__(self) -> str:
        return f"{self.name}"


class City(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    ibge_code = models.CharField(max_length=10, null=False, blank=False)

    class Meta:
        db_table: str = "city"
        verbose_name_plural: str = "cities"

    def __str__(self) -> str:
        return f"{self.name}"


class Country(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False)

    class Meta:
        db_table: str = "country"
        verbose_name_plural: str = "countries"

    def __str__(self) -> str:
        return f"({self.code}) {self.name}"