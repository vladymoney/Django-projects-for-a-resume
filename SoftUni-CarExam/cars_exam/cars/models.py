from django.core.validators import (
    MinLengthValidator,
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models


class Car(models.Model):
    CAR_TYPE_LEN = 10

    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    MODEL_MIN_LEN = 2
    MODEL_MAX_LEN = 20

    YEAR_MIN_VALUE = 1980
    YEAR_MAX_VALUE = 2049
    YEAR_ERROR_MSG = f"Year must be between {YEAR_MIN_VALUE} and {YEAR_MAX_VALUE}"

    PRICE_MIN_VALUE = 1
    PRICE_ERROR_MSG = f"Price cannot be below {PRICE_MIN_VALUE}"

    CHOICES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )
    type = models.CharField(
        max_length=CAR_TYPE_LEN, choices=CHOICES, null=False, blank=False
    )
    model = models.CharField(
        max_length=MODEL_MAX_LEN,
        validators=(MinLengthValidator(MODEL_MIN_LEN),),
        null=False,
        blank=False,
    )
    year = models.IntegerField(
        validators=(
            MinValueValidator(YEAR_MIN_VALUE, message=YEAR_ERROR_MSG),
            MaxValueValidator(YEAR_MAX_VALUE, message=YEAR_ERROR_MSG),
        )
    )
    image_url = models.URLField(
        verbose_name="Image URL",
        null=False,
        blank=False,
    )
    price = models.FloatField(
        validators=(MinValueValidator(PRICE_MIN_VALUE, message=PRICE_ERROR_MSG),)
    )
