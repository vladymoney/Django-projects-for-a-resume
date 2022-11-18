from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path("admin/", admin.site.urls),
    path("", include("cars_exam.common.urls")),
    path("profile/", include("cars_exam.my_profile.urls")),
    path("car/", include("cars_exam.cars.urls")),

)
