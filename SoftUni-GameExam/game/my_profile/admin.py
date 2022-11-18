from django.contrib import admin

from game.my_profile.models import Profile


# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "age",
        "password",
        "first_name",
        "last_name",
        "profile_picture",
    )
