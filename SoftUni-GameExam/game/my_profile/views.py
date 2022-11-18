from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from game.my_game.models import Game
from game.my_profile.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from game.my_profile.models import Profile


def create_profile(request):
    form = CreateProfileForm()

    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    context = {"form": form}
    return render(
        request, template_name="my_profile/create-profile.html", context=context
    )


def profile_details(request):
    profile = Profile.objects.first()
    total_games = Game.objects.all()

    total_rating = sum([game.rating for game in total_games])

    try:
        average = total_rating / len(total_games)
    except ZeroDivisionError:
        average = 0.0

    context = {"profile": profile, "total_games": total_games, "average": average}
    return render(
        request, template_name="my_profile/details-profile.html", context=context
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
        request, template_name="my_profile/edit-profile.html", context=context
    )


def delete_profile(request):
    profile = Profile.objects.first()
    form = DeleteProfileForm(instance=profile)

    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        return redirect("home-page")
    context = {"form": form}
    return render(
        request, template_name="my_profile/delete-profile.html", context=context
    )
