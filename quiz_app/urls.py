from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="quiz-home"),
    path('about/', views.about, name="quiz-about"),
    path('quiz/', views.quiz, name="quiz-quiz"),
    path('results/<int:score>', views.results, name="quiz-results"),
]