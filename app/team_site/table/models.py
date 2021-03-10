from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    games = models.PositiveSmallIntegerField()
    wins = models.PositiveSmallIntegerField()
    draws = models.PositiveSmallIntegerField()
    loses = models.PositiveSmallIntegerField()
    goals_scored = models.PositiveSmallIntegerField()
    goals_allowed = models.PositiveSmallIntegerField()
    points = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name}'
