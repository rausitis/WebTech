# Generated by Django 5.1.1 on 2024-11-03 15:13

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0004_castmembers_moviestar_content_duration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='phoneNo',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Phone Number'),
        ),
    ]