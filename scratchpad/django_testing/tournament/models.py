from datetime import date
from django.db import models
from random import randint, sample


class Team(models.Model):
    name = models.CharField(max_length=64)


class Player(models.Model):
    height = models.FloatField()
    name = models.CharField(max_length=64)
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='player_team')


class Game(models.Model):
    home_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='game_at_home')
    home_points = models.IntegerField()
    rival_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='rival_game')
    rival_points = models.IntegerField()
    date = models.DateField()


def clear_db():
    for team in Team.objects.all():
        team.delete()


def populate_db():
    clear_db()
    for i in range(1, 3):
        team = create_team(i)
        for j in range(1, randint(4, 6)):
            create_player(team, j)
    create_games()


def create_team(num: int) -> Team:
    name = f"Team #{num}"
    return Team.objects.create(name=name)


def create_player(team: Team, num: int) -> Player:
    name = f"{team.name} Player {num}"
    return Player.objects.create(
        name=name,
        height=randint(17000, 20000) / 100,
        team=team,
    )


def create_games():
    team_ids = [team.id for team in Team.objects.all()]
    for _ in range(3):
        teams = sample(team_ids, k=2)
        Game.objects.create(
            home_team=Team.objects.get(id=teams[0]),
            home_points=randint(0, 10),
            rival_team=Team.objects.get(id=teams[1]),
            rival_points=randint(0, 10),
            date=date(
                year=randint(-4200, 2050),
                month=randint(1, 12),
                day=randint(1, 28)
            )
        )
