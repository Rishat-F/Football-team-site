from django.shortcuts import render

from datetime import date
from .models import Player

# Create your views here.
def calculate_age(dob):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

def by_points(object):
    if object.games != 0:
        points = object.goals + object.passes
        return points
    else:
        return -1

def roster_page(request):
    players = list(Player.objects.all())

    for player in players:
        player.points = player.goals + player.passes
        player.age = calculate_age(player.dob)
    players.sort(key=by_points, reverse=True)
    return render(request, 'roster/roster.html', context={'players': players})
