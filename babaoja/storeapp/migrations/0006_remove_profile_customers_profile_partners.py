# Generated by Django 4.2 on 2025-03-25 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0005_remove_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='customers',
        ),
        migrations.AddField(
            model_name='profile',
            name='partners',
            field=models.ManyToManyField(blank=True, related_name='customers', to='storeapp.profile'),
        ),
    ]
