# Generated by Django 4.0.1 on 2023-05-28 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_trip_bus_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='bus_id',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]