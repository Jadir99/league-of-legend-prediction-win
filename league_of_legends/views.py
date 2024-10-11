from django.shortcuts import render
from django.http import HttpResponse
from .models import Champion
from .models import Participant
from .models import Game
from django.db.models import Count

from django.db.models.functions import ExtractMonth
# def hello(request):
#     # return HttpResponse('jadir is the best in django')
#     return render(request, 'test.html',{'test':5})



def champs(request):
    champs=Champion.objects.all()
    count=Champion.objects.count()
    games = Game.objects.values('duration').annotate(count=Count('duration')).order_by('duration')
    # Get game counts per month from the 'Participant' model
    games_by_month = Participant.objects.annotate(
        month=ExtractMonth('date_game')  # Extracting the month from the 'date_game' field
    ).values('month').annotate(
        total_games=Count('id')  # Counting the number of games per month
    ).order_by('month')  # Ordering by the month

    # for game in games:
    #     print(f"Duration: {game['duration']}, Count: {game['count']}")
    return render(request,"test.html",{'champs':champs,'count':count,'games':games,'games_by_month':games_by_month})
