from django.shortcuts import render, redirect

from music.my_album.models import Album
from music.my_profile.forms import CreateProfileForm, DeleteProfileForm
from music.my_profile.models import Profile


def home_page(request):
    user = Profile.objects.first()
    if not user:
        form = CreateProfileForm()
        if request.method == "POST":
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, "my_profile/home-with-profile.html")
        context = {"form": form, "user": user}
        return render(request, "my_profile/home-no-profile.html", context)
    albums = Album.objects.all()
    context = {"albums": albums}
    return render(request, "my_profile/home-with-profile.html", context)


def profile_details(request):
    user = Profile.objects.first()
    albums_count = Album.objects.count()

    context = {"user": user, "albums_count": albums_count}
    return render(request, "my_profile/profile-details.html", context)


def delete_profile(request):
    profile = Profile.objects.first()
    form = DeleteProfileForm(instance=profile)

    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    context = {"form": form}
    return render(request, "my_profile/profile-delete.html", context)
