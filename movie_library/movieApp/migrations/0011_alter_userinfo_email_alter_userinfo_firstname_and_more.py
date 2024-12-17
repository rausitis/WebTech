# Generated by Django 5.0 on 2024-12-17 19:32

import django.core.validators
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0010_moviemakers_contentnr_moviemakers_nr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator('^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$', message='Enter a valid email address.')]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='firstname',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Za-z]+$', message='First name must contain only letters.')]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='lastname',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Za-z]+$', message='Last name must contain only letters.')]),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phoneNo',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='Phone Number'),
        ),
    ]