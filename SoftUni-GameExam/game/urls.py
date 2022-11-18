from django.contrib import admin
from django.urls import path, include


urlpatterns = (
    path("admin/", admin.site.urls),
    path("", include("game.common.urls")),
    path("profile/", include("game.my_profile.urls")),
    path("game/", include("game.my_game.urls")),
)
