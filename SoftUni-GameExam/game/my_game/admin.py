from django.contrib import admin

from game.my_game.models import Game


# Register your models here.


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "rating",
        "max_level",
        "image_url",
        "summary",
    )
