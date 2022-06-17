from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.ClassroomDetailsList.postSave, name="postSave"),
        path('classroomDetail/', views.ClassroomDetailsList.ClassroomDetail, name="classroomDetail"),
        path('classroomAccessTeachers/', views.ClassroomDetailsList.ClassroomAccessTeachers, name="classroomAccessTeachers"),
        path('classroomAccessDetail/', views.ClassroomDetailsList.ClassroomAccessDetail, name="classroomAccessDetail"),
    ]