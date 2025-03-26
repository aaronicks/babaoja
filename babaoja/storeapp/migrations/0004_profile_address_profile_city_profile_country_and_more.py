# Generated by Django 4.2 on 2025-03-23 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0003_alter_product_category_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='Not Provided', max_length=150),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Not Provided', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default='Not Provided', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='Not Provided', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='Not Provided', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(default='Not Provided', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='zipcode',
            field=models.CharField(default='Not', max_length=6),
        ),
    ]
