from django.shortcuts import render

from .models import Team

# Create your views here.
def table_page(request):
    teams = Team.objects.all().order_by('-points', '-wins')
    k = 1
    for team in teams:
        team.position = k
        if team.name == 'Меркурио':
            team.status = 'our-team'
        k += 1
    return render(request, 'table/table.html', context={'teams': teams})
