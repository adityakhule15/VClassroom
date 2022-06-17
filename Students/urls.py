from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('postSave/', views.StudentDetailsList.postSave, name="postSave"),
        path('studentDetails/', views.StudentDetailsList.StudentDetails, name="studentDetails"),
        path('update/', views.StudentDetailsList.update, name="update"),
        path('updateImage/', views.StudentDetailsList.updateImage, name="updateImage"),
        path('postClassAccess/', views.ClassroomAccess.postClassAccess, name="postClassAccess"),
        path('studentClassAccessDetails/', views.ClassroomAccess.StudentClassAccessDetails, name="studentClassAccessDetails"),
        path('deleteAccess/', views.ClassroomAccess.deleteAccess, name="deleteAccess"),
    ]