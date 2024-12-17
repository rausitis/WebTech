from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
# from TwoFAUserApp.models import TwoFAUser
import random
# Individual extension SG
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator

class UserInfoManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)


class UserInfo(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, validators=[MinLengthValidator(1), MaxLengthValidator(40)])
    email = models.EmailField(unique=True, validators=[EmailValidator(), MinLengthValidator(1), MaxLengthValidator(60)])
    firstname = models.CharField(max_length=255, validators=[MinLengthValidator(1), MaxLengthValidator(40)])
    lastname = models.CharField(max_length=255, validators=[MinLengthValidator(1),MaxLengthValidator(40)])
    createdAt = models.DateTimeField(default=timezone.now)
    modifiedAt = models.DateTimeField(auto_now=True)
    phoneNo = PhoneNumberField(_("Phone Number"), blank=True, null=True, validators=[MinLengthValidator(8), MaxLengthValidator(15)])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserInfoManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Content(models.Model):
    title = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    description = models.TextField(max_length=5000, validators=[MinLengthValidator(1)])
    matureContent = models.BooleanField()
    type = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    country = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    genre = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    year = models.PositiveIntegerField()
    duration = models.DurationField()
    seasonsNo = models.PositiveIntegerField()
    createdAt = models.DateTimeField(default=timezone.now)
    modifiedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(UserInfo, on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True, related_name='createdContent')

    modifiedBy = models.ForeignKey(UserInfo, on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True, related_name='modifiedContent')

    def __str__(self):
        return self.title


class CastMembers(models.Model):
    nr = models.IntegerField()
    contentNr = models.IntegerField()
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    character = models.TextField(max_length=255)
    contentId = models.IntegerField()
    createdAt = models.DateTimeField(default=timezone.now)
    modifiedAt = models.DateTimeField(auto_now=True)
    movieStar = models.BooleanField()
    createdBy = models.ForeignKey(UserInfo, on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True, related_name='createdCast')
    modifiedBy = models.ForeignKey(UserInfo, on_delete=models.SET_NULL,
                                   null=True,
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
    nr = models.IntegerField()
    contentNr = models.IntegerField()
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255)
    contentId = models.IntegerField()
    createdAt = models.DateTimeField(default=timezone.now)
    modifiedAt = models.DateTimeField(auto_now=True)
    createdBy = models.ForeignKey(UserInfo, on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True,
                                  related_name='createdMovieMakers')
    modifiedBy = models.ForeignKey(UserInfo, on_delete=models.SET_NULL,
                                   null=True,
                                   blank=True,
                                   related_name='modifiedMovieMakers')

    def __str__(self):
        return f"{self.firstname} {self.lastname} as {self.position}"

# Models for 2FA - individual extenstion EF part


class Code(models.Model):
    codenumber = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.codenumber)

    # overriding save method

    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items = []

        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)

        code_string = "".join(str(item) for item in code_items)
        self.codenumber = code_string
        super().save(*args, **kwargs)


# AuthToken, Roles, Admin covered by Django automatically
# _str_ used to return full string for username, title
# _str_ used to return character - actor, username - favorite content
# CreatedBy, modifiedBy refering to built-in Admin table in User
