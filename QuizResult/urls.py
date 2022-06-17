from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.QuizResultDetailsList.postSave, name="postSave"),
        path('quizResultDetails/', views.QuizResultDetailsList.QuizResultDetails, name="quizResultDetails"),
        path('quizResult/', views.QuizResultDetailsList.QuizResult, name="quizResult"),
    ]