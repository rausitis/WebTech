# Generated by Django 5.1.1 on 2024-10-22 01:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=5000)),
                ('matureContent', models.BooleanField()),
                ('type', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('year', models.PositiveIntegerField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CastMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('castMember', models.CharField(max_length=255)),
                ('character', models.CharField(max_length=255)),
                ('contentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieApp.content')),
            ],
        ),
    ]