from django.db import models
from datetime import date

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=3, blank=True)

    GOALKEEPER = 'gk'
    FIELD_PLAYER = 'un'
    POSITION_CHOICES = [
        (GOALKEEPER, 'вратарь'),
        (FIELD_PLAYER, 'полевой игрок'),
    ]

    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    games = models.PositiveSmallIntegerField()
    goals = models.PositiveSmallIntegerField()
    passes = models.PositiveSmallIntegerField()
    pm = models.PositiveSmallIntegerField(blank=True, default=0)
    photo = models.ImageField(upload_to='images/players_photos', default='images/players_photos/no_photo.png')
    height = models.CharField(max_length=3, default='100')
    weight = models.CharField(max_length=3, default='100')
    dob = models.DateField(default=date.today)

    def __str__(self):
        return f'{self.name}'
