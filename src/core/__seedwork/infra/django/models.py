import uuid
from django.db import models
from django.utils import timezone
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords


class BaseModel(SafeDeleteModel):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True
        ordering: list[str] = ["-created_at"]
        get_latest_by: str = "created_at"


class BaseModelWithHistory(BaseModel):
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
        ordering: list[str] = ["-created_at"]
        get_latest_by: str = "created_at"


class BaseModelWithTenant(BaseModel):
    tenant = models.ForeignKey(
        "tenant_django_app.Tenant",
        on_delete=models.PROTECT,
        related_name="%(class)s",
    )

    class Meta:
        abstract = True
        ordering: list[str] = ["-created_at"]
        get_latest_by: str = "created_at"


class BaseModelWithTenantAndHistory(BaseModelWithTenant):
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
        ordering: list[str] = ["-created_at"]
        get_latest_by: str = "created_at"