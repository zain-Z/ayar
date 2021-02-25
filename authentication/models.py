from django.db.models.signals import post_save
from backend import settings
from django.db import models
from django_countries.fields import CountryField
from django.core.validators import EMPTY_VALUES

# Create your models here.
import json
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.core.validators import RegexValidator
from rest_framework_simplejwt.tokens import RefreshToken
from .validators import validate_file_extension, validate_image_extension
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class UserManager(BaseUserManager):

    def create_user(self,  username, email,
                    password=None, confirm_password=True):

        if username is None:
            raise TypeError('Users should have a username')

        if email is None:
            raise TypeError('Users should have an Email')

        user = self.model(
            username=username,

            email=self.normalize_email(email),

        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}


class User(AbstractBaseUser, PermissionsMixin):

    LANGUAGE_OPTIONS = [
        ('ARABIC', 'ARABIC'),
        ('ENGLISH', 'ENGLISH'),
    ]

    language = models.CharField(
        choices=LANGUAGE_OPTIONS, max_length=255, default='ARABIC')

###############################################################################

    USER_CHOICE = (
        ("Developer", "Developer"),
        ("Customer", "Customer"),
    )
    user_type = models.CharField(
        choices=USER_CHOICE, default="Developer", max_length=30)

###############################################################################

    username = models.CharField(max_length=255, unique=True, db_index=True)

###############################################################################

    COUNTRY_CODE_CHOICE = (
        ('SAUDIARABIA', "+966"),
        ('JORDAN', "+962"),
        ('UNITEDARABEMIRATES', "+971"),
        ('BAHRAIN', "+973"),
        ('IRAQ', "+964"),
    )
    country_code = models.CharField(null=True, blank=True,
                                    choices=COUNTRY_CODE_CHOICE,
                                    default='SAUDIARABIA', max_length=100)
    country = CountryField(null=True, blank=True,
                           max_length=200, default="")
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,14}$',
        message="Phone number must be entered in the format: '+999999999'.\
             Up to 14 digits allowed.")
    phone = models.CharField(
        validators=[phone_regex],
        max_length=17, unique=True, blank=True, null=True)

    def __str__(self):
        return str(self.phone)

###############################################################################

    email = models.EmailField(max_length=255, unique=True, db_index=True)

###############################################################################

    job = models.CharField(max_length=255,
                           db_index=True, default=' ')

###############################################################################

    skills = models.TextField(null=True, blank=True)

    @property
    def list(self):
        return json.loads(self.skills)

    @list.setter
    def list(self, value):
        self.skills = json.dumps(self.list + value)

###############################################################################

    profile_image = models.ImageField(
        blank=True, null=True, validators=[validate_image_extension],
        upload_to='uploaded_files/')

###############################################################################

    background_image = models.ImageField(
        blank=True, null=True, validators=[validate_image_extension],
        upload_to='uploaded_files/')

###############################################################################

    about_me = models.TextField(blank=True, null=True)

###############################################################################

    work_title = models.CharField(
        max_length=255, null=True, default=" ", blank=True)

    work_description = models.TextField(
        null=True, default="", blank=True)

    work_url = models.CharField(
        max_length=255, blank=True, null=True)

    work_date = models.DateField(
        editable=True, blank=True, null=True, auto_now=False,
        auto_now_add=False)

    work_skills = models.TextField(default="", blank=True, null=True)

    @property
    def list(self):
        return json.loads(self.work_skills)

    @list.setter
    def list(self, value):
        self.work_skills = json.dumps(self.list + value)

    upload_work_files = models.FileField(
        blank=True, null=True, validators=[validate_file_extension],
        upload_to='uploaded_files/')

    @property
    def list(self):
        return json.loads(self.upload_work_files)

    @list.setter
    def list(self, value):
        self.upload_work_files = json.dumps(self.list + value)

    work_dict = {work_title: work_description}
    print(work_dict)

###############################################################################

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return str(self.email)

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }