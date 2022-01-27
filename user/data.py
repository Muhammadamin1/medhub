from django.db import models


class UserGenderChoices(models.IntegerChoices):
    MALE = 1, 'Male',
    FEMALE = 2, 'Female',