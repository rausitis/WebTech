from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Movie(models.Model):
    country = models.ManyToManyField(to=Country,related_name="Movies")
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    matureContent = models.BooleanField()
    type = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    duration = models.DurationField()
    seasonsNo = models.PositiveIntegerField()
    image = models.ImageField(upload_to="images/",blank=True,null=True)

    def __str__(self):
        return self.title


class User(AbstractUser):
    age = models.PositiveIntegerField(default=True)
    gender = models.CharField(max_length=255,default="")


