# Generated by Django 5.1.3 on 2024-11-14 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylib', '0002_alter_user_age_alter_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
