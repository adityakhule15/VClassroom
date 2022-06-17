from django.urls import path
from . import views

''' Creating URLS for call functions '''

urlpatterns = [
        path('pdfPostSave/', views.NotesDetailsList.pdf_postSave, name="pdf_postSave"),
        path('docPostSave/', views.NotesDetailsList.doc_postSave, name="doc_postSave"),
        path('docxPostSave/', views.NotesDetailsList.docx_postSave, name="docx_postSave"),
        path('mp3postSave/', views.NotesDetailsList.mp3postSave, name="mp3postSave"),
        path('notesQuestionPapersDetails/', views.NotesDetailsList.NotesQuestionPapersDetails, name="notesQuestionPapersDetails"),
        path('notesDetails/', views.NotesDetailsList.NotesDetails, name="NotesDetails"),
        path('audioNotesDetails/', views.NotesDetailsList.AudioNotesDetails, name="audioNotesDetails"),
    ]