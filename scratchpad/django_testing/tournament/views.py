from django.shortcuts import render, Http404
from django.views import View

from . import models


class MainView(View):
    def get(self, request, *args, **kwargs):
        models.populate_db()
        context = {
            "games": models.Game.objects.all(),
        }
        return render(request, "tournament/index.html", context=context)


class TeamView(View):
    def get(self, request, team_id, *args, **kwargs):
        try:
            team = models.Team.objects.get(id=team_id)
        except models.Team.DoesNotExist:
            raise Http404
        context = {
            "team": team,
            "players": models.Player.objects.filter(team=team)
        }
        return render(request, "tournament/team_info.html", context=context)
