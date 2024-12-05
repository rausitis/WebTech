from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class UserInfo(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=255)
    createdAt = models.DateTimeField(default=timezone.now)
    modifiedAt = models.DateTimeField(auto_now=True)
    phoneNo = PhoneNumberField(_("Phone Number"), blank=True, null=True)

    def __str__(self):
        return self.username


class Content(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    matureContent = models.BooleanField()
    type = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    duration = models.DurationField()
    seasonsNo = models.PositiveIntegerField()
    createdAt = models.DateTimeField(default=timezone.now)
    modifiedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                  blank=True, related_name='createdContent')
    modifiedBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                   blank=True, related_name='modifiedContent')

    def __str__(self):
        return self.title


class CastMembers(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    character = models.TextField(max_length=255)
    contentId = models.ForeignKey(Content, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=timezone.now)
    modifiedAt = models.DateTimeField(auto_now=True)
    movieStar = models.BooleanField()
    createdBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                  blank=True, related_name='createdCast')
    modifiedBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                   blank=True, related_name='modifiedCast')

    def __str__(self):
        return f"{self.firstname} {self.lastname} as {self.character}"


class FavoriteContent(models.Model):
    username = models.ForeignKey(UserInfo, on_delete=models.CASCADE,
                                 related_name='favorites')
    contentId = models.ForeignKey(Content, on_delete=models.CASCADE,
                                  related_name='favored_by')
    createdAt = models.DateTimeField(default=timezone.now)
    modifiedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.content.title}"


class MovieMakers(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255)
    contentId = models.ForeignKey(Content, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(default=timezone.now)
    modifiedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                  blank=True,
                                  related_name='createdMovieMakers')
    modifiedBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                   blank=True,
                                   related_name='modifiedMovieMakers')

    def __str__(self):
        return f"{self.firstname} {self.lastname} as {self.position}"


# AuthToken, Roles, Admin covered by Django automatically
# _str_ used to return full string for username, title
# _str_ used to return character - actor, username - favorite content
# CreatedBy, modifiedBy refering to built-in Admin table in User
