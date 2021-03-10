from django.shortcuts import render

from .models import Match

# Create your views here.
def calendar_page(request):
    matches = Match.objects.order_by('-date')
    return render(request, 'tcalendar/calendar.html', context={'matches': matches})
