# Generated by Django 5.0 on 2024-12-16 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0007_castmembers_nr'),
    ]

    operations = [
        migrations.AddField(
            model_name='castmembers',
            name='contentNr',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
