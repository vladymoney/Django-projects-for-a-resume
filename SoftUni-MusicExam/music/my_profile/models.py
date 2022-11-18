from django.core.validators import MinValueValidator, RegexValidator, MinLengthValidator
from django.db import models


class Profile(models.Model):
    USERNAME_MAX_LEN = 15
    USERNAME_MIN_LEN = 2
    USERNAME_ERROR = "Ensure this value contains only letters, numbers, and underscore."
    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=[
            MinLengthValidator(USERNAME_MIN_LEN),
            RegexValidator(
                "^\\w+$",
                message=USERNAME_ERROR,
            ),
        ],
    )
    email = models.EmailField()
    age = models.IntegerField(
        validators=(MinValueValidator(AGE_MIN_VALUE),),
        null=True,
        blank=True,
    )
