from django.shortcuts import render, redirect

from cars_exam.cars.forms import CreateCarForm, EditCarForm, DeleteCarForm
from cars_exam.cars.models import Car
from cars_exam.my_profile.models import Profile


def create_car(request):
    profile = Profile.objects.first()
    form = CreateCarForm()

    if request.method == "POST":
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    context = {"form": form, "profile": profile}
    return render(request, template_name="cars/car-create.html", context=context)


def car_details(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.get(pk=pk)
    context = {"car": car, "profile": profile}
    return render(request, template_name="cars/car-details.html", context=context)


def edit_car(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.get(pk=pk)
    form = EditCarForm(instance=car)

    if request.method == "POST":
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    context = {"profile": profile, "car": car, "form": form}
    return render(request, template_name="cars/car-edit.html", context=context)


def delete_car(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.get(pk=pk)
    form = DeleteCarForm(instance=car)

    if request.method == "POST":
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    context = {"profile": profile, "car": car, "form": form}
    return render(request, template_name="cars/car-delete.html", context=context)
