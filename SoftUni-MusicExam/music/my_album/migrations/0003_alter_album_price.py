# Generated by Django 4.1.2 on 2022-10-19 12:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_album", "0002_alter_album_image_url_alter_album_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="album",
            name="price",
            field=models.FloatField(
                validators=[
                    django.core.validators.MinValueValidator(
                        0.0, message="The price cannot be below 0.0"
                    )
                ]
            ),
        ),
    ]
