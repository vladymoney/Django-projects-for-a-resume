from django.shortcuts import render

from cars_exam.my_profile.models import Profile
from cars_exam.cars.models import Car


def index(request):
    profile = Profile.objects.first()
    context = {"profile": profile}
    return render(request, template_name="common/index.html", context=context)


def catalogue(request):
    cars = Car.objects.all()
    profile = Profile.objects.first()
    context = {"cars": cars, "profile": profile}
    return render(request, template_name="common/catalogue.html", context=context)
