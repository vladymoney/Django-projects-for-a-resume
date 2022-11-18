from django.urls import path
from music.my_album.views import *

urlpatterns = (
    path("add/", add_album, name="add-album"),
    path("details/<str:pk>/", album_details, name="album-details"),
    path("edit/<str:pk>/", edit_album, name="edit-album"),
    path("delete/<str:pk>/", delete_album, name="delete-album"),
)
