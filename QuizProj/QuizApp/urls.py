from django.urls import path     #importing path
from . import views      #importing views from current directory

urlpatterns = [
    path('', views.home, name='home'), #path to views.py of models
    path('api/get-quiz/' , views.get_quiz , name="get_quiz"), #(1)path to views.py of API
    path('quiz/', views.quiz, name="quiz") #(2) path to views.py of to render web page
]