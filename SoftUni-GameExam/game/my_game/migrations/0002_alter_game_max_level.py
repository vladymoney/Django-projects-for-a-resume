# Generated by Django 4.1.1 on 2022-10-01 15:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_game", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="max_level",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MinValueValidator(1)],
            ),
        ),
    ]