# Generated by Django 4.2 on 2024-11-25 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skapp', '0003_imagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='House_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('area', models.IntegerField(max_length=200)),
                ('beds', models.IntegerField(max_length=200)),
                ('baths', models.IntegerField(max_length=20)),
                ('garages', models.IntegerField(max_length=20)),
            ],
        ),
    ]
