# Generated by Django 4.2 on 2024-11-26 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skapp', '0008_rename_service_booking_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='services',
            new_name='offer',
        ),
    ]
