# Generated by Django 4.2 on 2024-11-26 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skapp', '0007_rename_servuce_booking_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='service',
            new_name='services',
        ),
    ]
