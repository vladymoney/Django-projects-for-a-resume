from django.shortcuts import render, redirect

from cars_exam.cars.models import Car
from cars_exam.my_profile.forms import (
    CreateProfileForm,
    EditProfileForm,
    DeleteProfileForm,
)
from cars_exam.my_profile.models import Profile


def create_profile(request):
    form = CreateProfileForm()

    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    context = {"form": form}
    return render(
        request, template_name="my_profile/profile-create.html", context=context
    )


def profile_details(request):
    profile = Profile.objects.first()
    total_cars = Car.objects.all()

    total_price = sum([car.price for car in total_cars])

    context = {"profile": profile, "total_cars": total_cars, "total_price": total_price}
    return render(
        request, template_name="my_profile/profile-details.html", context=context
    )


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditProfileForm(instance=profile)

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("details-profile")

    context = {"profile": profile, "form": form}
    return render(
        request, template_name="my_profile/profile-edit.html", context=context
    )


def delete_profile(request):
    profile = Profile.objects.first()
    form = DeleteProfileForm(instance=profile)

    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {"form": form, "profile": profile}
    return render(
        request, template_name="my_profile/profile-delete.html", context=context
    )
