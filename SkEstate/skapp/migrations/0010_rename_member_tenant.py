# Generated by Django 4.2 on 2024-11-27 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skapp', '0009_rename_services_booking_offer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member',
            new_name='Tenant',
        ),
    ]
