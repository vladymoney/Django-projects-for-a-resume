from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Game(models.Model):
    TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15
    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5.0
    RATING_MIN_VALUE_MSG = (
        f"The rating can be between {RATING_MIN_VALUE} and {RATING_MAX_VALUE}"
    )

    RATING_MAX_VALUE_MSG = (
        f"The rating can be between {RATING_MIN_VALUE} and {RATING_MAX_VALUE}"
    )

    MIN_LVL_VALUE = 1
    MIN_LVL_MSG = "The max level cannot be below 1"

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
        null=True,
        blank=True,
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        choices=(
            ("Action", "Action"),
            ("Adventure", "Adventure"),
            ("Puzzle", "Puzzle"),
            ("Strategy", "Strategy"),
            ("Sports", "Sports"),
            ("Board/Card Game", "Board/Card Game"),
            ("Other", "Other"),
        ),
        null=True,
        blank=True,
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(RATING_MIN_VALUE, message=RATING_MIN_VALUE_MSG),
            MaxValueValidator(RATING_MAX_VALUE, message=RATING_MAX_VALUE_MSG),
        ),
        null=True,
        blank=True,
    )

    max_level = models.IntegerField(
        validators=(MinValueValidator(MIN_LVL_VALUE, message=MIN_LVL_MSG),),
        verbose_name="Max Level",
        null=True,
        blank=True,
    )

    image_url = models.URLField(null=False, blank=False, verbose_name="Image URL")

    summary = models.TextField(
        null=True,
        blank=True,
    )
