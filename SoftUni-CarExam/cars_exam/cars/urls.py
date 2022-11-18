from django.urls import path, include
from cars_exam.cars.views import *

urlpatterns = (
    path("create/", create_car, name="create-car"),
    path('<int:pk>/', include([
        path('details/', car_details, name='details-car'),
        path('edit/', edit_car, name='edit-car'),
        path('delete/', delete_car, name='delete-car')],)
    ))
