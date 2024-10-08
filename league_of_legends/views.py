from django.shortcuts import render
from django.http import HttpResponse
from .models import Champion
# def hello(request):
#     # return HttpResponse('jadir is the best in django')
#     return render(request, 'test.html',{'test':5})



def champs(request):
    champs=Champion.objects.all()
    return render(request,"test.html",{'champs':champs})
