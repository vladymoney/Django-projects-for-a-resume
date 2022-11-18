from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class Profile(models.Model):
    MIN_USERNAME_LEN = 2
    MAX_USERNAME_LEN = 10
    USERNAME_ERROR_MSG = f"The username must be a minimum of {MIN_USERNAME_LEN} chars"
    MIN_AGE_VALUE = 18
    AGE_ERROR_MSG = f"The age cannot be below {MIN_AGE_VALUE}"
    MAX_PASS_LEN = 30
    FIRST_NAME_LEN = 30
    LAST_NAME_LEN = 30

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        validators=(MinLengthValidator(MIN_USERNAME_LEN, message=USERNAME_ERROR_MSG),),
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(MinValueValidator(MIN_AGE_VALUE, message=AGE_ERROR_MSG),),
    )
    password = models.CharField(
        max_length=MAX_PASS_LEN,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_LEN,
        verbose_name="First Name",
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_LEN,
        verbose_name="Last Name",
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        verbose_name="Profile Picture",
        null=True,
        blank=True,
    )
