from django.urls import path
from cars_exam.common.views import *

urlpatterns = (
    path("", index, name="index"),
    path("catalogue/", catalogue, name="catalogue"),
)
