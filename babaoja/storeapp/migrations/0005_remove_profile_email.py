# Generated by Django 4.2 on 2025-03-23 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0004_profile_address_profile_city_profile_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
