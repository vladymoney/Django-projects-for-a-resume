from django.urls import path

from game.my_profile.views import *

urlpatterns = (
    path("create/", create_profile, name="create-profile"),
    path("details/", profile_details, name="details-profile"),
    path("edit/", edit_profile, name="edit-profile"),
    path("delete/", delete_profile, name="delete-profile"),
)
