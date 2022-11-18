from django.shortcuts import render, redirect

from game.my_game.forms import CreateGameForm, EditGameForm, DeleteGameForm
from game.my_game.models import Game


def create_game(request):
    form = CreateGameForm()

    if request.method == "POST":
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {"form": form}
    return render(request, template_name="my_game/create-game.html", context=context)


def game_details(request, pk):
    game = Game.objects.get(pk=pk)
    context = {"game": game}

    return render(request, template_name="my_game/details-game.html", context=context)


def edit_game(request, pk):
    game = Game.objects.get(pk=pk)
    form = EditGameForm(instance=game)

    if request.method == "POST":
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {"game": game, "form": form}
    return render(request, template_name="my_game/edit-game.html", context=context)


def delete_game(request, pk):
    game = Game.objects.get(pk=pk)
    form = DeleteGameForm(instance=game)

    if request.method == "POST":
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
        return redirect("dashboard")
    context = {"game": game, "form": form}
    return render(request, template_name="my_game/delete-game.html", context=context)
