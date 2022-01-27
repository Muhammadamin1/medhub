from django.db import models
from django.utils.translation import gettext_lazy as _

from user.data import UserGenderChoices


class Interrogator(models.Model):
    username = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='interrogator', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)


class Responder(models.Model):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True,
                                error_messages={
                                    'unique': _("A user with that username already exists.")})
    birth_date = models.DateField()
    gender = models.PositiveSmallIntegerField(choices=UserGenderChoices.choices, default=UserGenderChoices.MALE)
    photo = models.ImageField(upload_to='responder', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
