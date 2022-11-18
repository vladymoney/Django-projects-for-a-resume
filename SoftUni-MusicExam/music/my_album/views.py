from django.shortcuts import render, redirect

from music.my_album.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteAlbum
from music.my_album.models import Album


def add_album(request):
    form = AlbumCreateForm()

    if request.method == "POST":
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    context = {"form": form}
    return render(request, "my_album/add-album.html", context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {"album": album}
    return render(request, "my_album/album-details.html", context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    form = AlbumEditForm(instance=album)

    if request.method == "POST":
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    context = {"form": form, "album": album}
    return render(request, "my_album/edit-album.html", context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    form = AlbumDeleteAlbum(instance=album)

    if request.method == "POST":
        form = AlbumDeleteAlbum(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    context = {"form": form, "album": album}
    return render(request, "my_album/delete-album.html", context)
