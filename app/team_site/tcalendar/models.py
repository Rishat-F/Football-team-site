from django.db import models

# Create your models here.
class Match(models.Model):
    date = models.DateField()
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    result = models.CharField(max_length=5)
    stage = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.stage}. {self.team1} {self.result} {self.team2}'
