# Generated by Django 4.0.1 on 2023-03-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_trip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='distance',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='end',
            field=models.CharField(max_length=100, null=True),
        ),
    ]