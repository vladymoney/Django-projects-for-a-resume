from django.urls import path
from game.my_game.views import *

urlpatterns = (
    path("create/", create_game, name="create-game"),
    path("details/<pk>/", game_details, name="details-game"),
    path("edit/<pk>/", edit_game, name="edit-game"),
    path("delete/<pk>/", delete_game, name="delete-game"),
)
