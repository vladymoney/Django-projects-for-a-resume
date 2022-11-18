from django.urls import path
from game.common.views import *

urlpatterns = (
    path("", home, name="home-page"),
    path("dashboard/", dashboard, name="dashboard"),
)
