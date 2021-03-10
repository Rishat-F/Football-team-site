from django.shortcuts import render

from roster.models import Player
from roster.views import by_points

# Create your views here.
def index_page(request):
    players = list(Player.objects.all())
    players.sort(key=by_points, reverse=True)
    for player in players:
        player.points = player.goals + player.passes
        if player.position == "gk":
            player.position = "GK"
        else:
            player.position = ""
        if player.name == "Козлов Владислав":
            vlad = player
    players.insert(0, players.pop(players.index(vlad)))
    players[0].rank = "first"
    players[1].rank = "second"
    players[2].rank = "third"
    return render(request, 'index/index.html', context={'players': players[:3]})
