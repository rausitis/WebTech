# Generated by Django 5.1.3 on 2024-11-14 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(default='', max_length=255),
        ),
    ]
