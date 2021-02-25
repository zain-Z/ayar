from django.db import models
from authentication.models import User


# Create your models here.


class PersonalInfo(models.Model):

    username = models.Field(editable=False, blank=True)
    phone = models.Field(editable=False, blank=True)
    email = models.EmailField(
        max_length=255, unique=True, db_index=True, editable=False, blank=True)
    job = models.Field(editable=False, blank=True)
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='PersonalInfo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ['-updated_at']


class Language(models.Model):
    LANGUAGE_OPTIONS = [
        ('ARABIC', 'ARABIC'),
        ('ENGLISH', 'ENGLISH'),
    ]

    language = models.CharField(
        choices=LANGUAGE_OPTIONS, max_length=255, default='ARABIC')
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='Language')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ['-updated_at']


class Country(models.Model):
    COUNTRY_OPTIONS = [
        ('SAUDIARABIA', 'SAUDIARABIA'),
        ('JORDAN', 'JORDAN'),
        ('UNITEDARABEMIRATES', 'UNITEDARABEMIRATES'),
        ('BAHRAIN', 'BAHRAIN'),
        ('IRAQ', 'IRAQ'),
    ]

    country = models.CharField(
        choices=COUNTRY_OPTIONS, max_length=255, default='SAUDIARABIA')
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='Country')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ['-updated_at']


class Wallet(models.Model):

    total_balance = models.BigIntegerField(
        default=0, editable=False, blank=True)
    outstanding = models.BigIntegerField(default=0, editable=False, blank=True)
    available = models.BigIntegerField(default=0, editable=False, blank=True)
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='Wallet')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ['-updated_at']

    def save(self):
        self.available = self.total_balance - self.outstanding
        return self.available
