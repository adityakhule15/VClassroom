from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.QuizDetailsList.postSave, name="postSave"),
        path('scheduledQuiz/', views.QuizDetailsList.ScheduledQuiz, name="scheduledQuiz"),
        path('quizDetail/', views.QuizDetailsList.QuizDetail, name="quizDetail"),
        path('quizList/', views.QuizDetailsList.QuizList, name="quizList"),
    ]