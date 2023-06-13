# Generated by Django 4.0.1 on 2023-05-28 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0016_delete_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('start_lat', models.CharField(max_length=100)),
                ('start_lon', models.CharField(max_length=100)),
                ('end_lat', models.CharField(blank=True, max_length=100, null=True)),
                ('end_lon', models.CharField(blank=True, max_length=100, null=True)),
                ('distance', models.CharField(blank=True, max_length=100, null=True)),
                ('bus_id', models.CharField(default=None, max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]