# Generated by Django 4.0.1 on 2023-05-28 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_trip_bus_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='bus_id',
        ),
    ]
