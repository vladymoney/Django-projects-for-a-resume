from django.shortcuts import render

from game.my_game.models import Game
from game.my_profile import models


def home(request):
    profile = models.Profile.objects.first()
    context = {"profile": profile}
    return render(request, template_name="common/home-page.html", context=context)


def dashboard(request):
    games = Game.objects.all()
    context = {"games": games}
    return render(request, template_name="common/dashboard.html", context=context)
