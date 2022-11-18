from django.db import models

# Create your models here.
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    MIN_AGE_VALUE = 12
    MIN_AGE_MSG = "The age cannot be below 12"
    MAX_PASS_LEN = 30
    MAX_FIRST_NAME_LEN = 30
    MAX_LAST_NAME_LEN = 30

    email = models.EmailField(null=False, blank=False)

    age = models.IntegerField(
        validators=(MinValueValidator(MIN_AGE_VALUE, message=MIN_AGE_MSG),),
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_PASS_LEN,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LEN,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
