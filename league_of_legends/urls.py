from django.urls import path
from . import views

# url configuration 
urlpatterns=[
    path('champs/',views.champs),
    path('all/',views.all),
    path('',views.home)
]

