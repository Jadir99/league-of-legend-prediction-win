from django.shortcuts import render
from django.http import HttpResponse
from .models import Champion
from .models import Participant
from .models import Game
from django.db.models import Count,Avg

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
        month=ExtractMonth('date_game')  
    ).values('month').annotate(
        total_games=Count('id') 
    
    ).order_by('month')  
    # top 5 champions :
    top_5 = champs.order_by('-winrate')[:5]  # Adjust based on your model's attributes
    bad_5 = champs.order_by('winrate')[:5]

    #avg of kills each of towers dragon and champs ...
    # Get the average tower kills from the Game model
    avg_tower_kills = Game.objects.aggregate(avg_tower_kills=Avg('tower_kills'))['avg_tower_kills'] or 0
    avg_inhibitor_kills = Game.objects.aggregate(avg_inhibitor_kills=Avg('inhibitor_kills'))['avg_inhibitor_kills'] or 0
    avg_baron_kills = (Game.objects.aggregate(avg_baron_kills=Avg('baron_kills'))['avg_baron_kills'] )*100 or 0
    avg_dragon_kills = Game.objects.aggregate(avg_dragon_kills=Avg('dragon_kills'))['avg_dragon_kills'] or 0

    # for game in games:
    #     print(f"Duration: {game['duration']}, Count: {game['count']}")
    return render(request,"test.html",{
        'champs':champs,
        'count':count,
        'games':games,
        'games_by_month':games_by_month,
        'top_5':top_5,
        'bad_5':bad_5,
        'avg_tower_kills':avg_tower_kills,
        'avg_inhibitor_kills':avg_inhibitor_kills,
        'avg_baron_kills':avg_baron_kills,
        'avg_dragon_kills':avg_dragon_kills,
        })


def home(request):
    return render(request, 'index.html')

def all(request):
    champs=Champion.objects.all()
    for champ in champs:
        # Assuming champ.winrate is a percentage (0-100)
        champ.lossrate = 100 - champ.winrate  # Calculate loss rate
    return render(request,'champs.html',{'champs':champs})

