# Generated by Django 5.0.7 on 2024-07-30 14:11

import django.db.models.deletion
import django.utils.timezone
import simple_history.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_django_app', '0002_alter_user_options_remove_user_cpf_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('corporate_name', models.CharField(max_length=255)),
                ('fantasy_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('cnpj', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('car_spaces', models.IntegerField()),
                ('motorcycle_spaces', models.IntegerField()),
                ('have_car_wash', models.BooleanField(default=False)),
                ('is_24_hours', models.BooleanField(default=False)),
                ('is_covered', models.BooleanField(default=False)),
                ('is_open', models.BooleanField(default=False)),
                ('security_guard', models.BooleanField(default=False)),
                ('camera', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Tenant',
                'verbose_name_plural': 'Tenants',
                'db_table': 'tenant',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clients', to='user_django_app.user')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s', to='tenant_django_app.tenant')),
            ],
            options={
                'ordering': ['-created_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalTenant',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('corporate_name', models.CharField(max_length=255)),
                ('fantasy_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('cnpj', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('car_spaces', models.IntegerField()),
                ('motorcycle_spaces', models.IntegerField()),
                ('have_car_wash', models.BooleanField(default=False)),
                ('is_24_hours', models.BooleanField(default=False)),
                ('is_covered', models.BooleanField(default=False)),
                ('is_open', models.BooleanField(default=False)),
                ('security_guard', models.BooleanField(default=False)),
                ('camera', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Tenant',
                'verbose_name_plural': 'historical Tenants',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalVehicle',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('plate', models.CharField(max_length=7)),
                ('model', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='tenant_django_app.client')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('tenant', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='tenant_django_app.tenant')),
            ],
            options={
                'verbose_name': 'historical Vehicle',
                'verbose_name_plural': 'historical Vehicles',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalClient',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user_django_app.user')),
                ('tenant', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='tenant_django_app.tenant')),
            ],
            options={
                'verbose_name': 'historical client',
                'verbose_name_plural': 'historical clients',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('plate', models.CharField(max_length=7)),
                ('model', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant_django_app.client')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s', to='tenant_django_app.tenant')),
            ],
            options={
                'verbose_name': 'Vehicle',
                'verbose_name_plural': 'Vehicles',
                'db_table': 'vehicle',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pre_exit', models.DateTimeField(blank=True, null=True)),
                ('pre_entry', models.DateTimeField(blank=True, null=True)),
                ('entry', models.DateTimeField()),
                ('exit', models.DateTimeField()),
                ('value', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('date', models.DateField()),
                ('parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations_parking', to='tenant_django_app.tenant')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s', to='tenant_django_app.tenant')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations_vehicle', to='tenant_django_app.vehicle')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
                'db_table': 'reservation',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalReservation',
            fields=[
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('pre_exit', models.DateTimeField(blank=True, null=True)),
                ('pre_entry', models.DateTimeField(blank=True, null=True)),
                ('entry', models.DateTimeField()),
                ('exit', models.DateTimeField()),
                ('value', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('date', models.DateField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parking', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='tenant_django_app.tenant')),
                ('tenant', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='tenant_django_app.tenant')),
                ('vehicle', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='tenant_django_app.vehicle')),
            ],
            options={
                'verbose_name': 'historical Reservation',
                'verbose_name_plural': 'historical Reservations',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
