# Generated by Django 4.0.1 on 2023-03-17 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_userinfo_balance_alter_userinfo_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='contact',
            field=models.CharField(max_length=100),
        ),
    ]
