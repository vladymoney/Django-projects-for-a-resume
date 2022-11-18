# Generated by Django 4.1.2 on 2022-10-19 12:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_album", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="image_url",
            field=models.URLField(verbose_name="Image URL"),
        ),
        migrations.AlterField(
            model_name="album",
            name="price",
            field=models.FloatField(
                validators=[django.core.validators.MinValueValidator(0.0)]
            ),
        ),
    ]
