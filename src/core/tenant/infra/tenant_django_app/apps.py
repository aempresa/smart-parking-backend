from django.apps import AppConfig


class TenantDjangoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.tenant.infra.tenant_django_app'
