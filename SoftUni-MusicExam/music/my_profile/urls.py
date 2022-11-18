from django.urls import path
from music.my_profile.views import *

urlpatterns = (
    path("details/", profile_details, name="profile-details"),
    path("delete/", delete_profile, name="delete-profile"),
)
