# Generated by Django 4.0.1 on 2023-05-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_trip_bus_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='bus_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
