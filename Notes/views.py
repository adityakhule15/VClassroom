from .serializers import NotesDetailsSerializer
from Attendence.models import Notes
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt 
import base64
from django.conf import settings

 
@csrf_exempt
class NotesDetailsList(APIView):
    # Defining the function for posting Notes

    @csrf_exempt
    def pdf_postSave(request):
        title_of_notes=request.POST.get('title_of_notes')
        classroom_code=request.POST.get('classroom_code')
        prod=Notes()
        prod.teachers_userName_id=request.POST.get('teacher_userName')
        prod.classroom_code_id=classroom_code
        prod.title_of_notes=title_of_notes
        prod.type=request.POST.get('type')
        prod.decpriction_of_notes=request.POST.get('decpriction_of_notes')
        notes=request.POST['notes'],
        print(notes[0])
        notesdata = base64.b64decode(notes[0])
        print(title_of_notes)
        path = settings.MEDIA_ROOT + '/all_notes/' + title_of_notes + classroom_code + '.pdf'
        print(path)
        with open(path, 'wb') as f:
            f.write(notesdata)
        prod.notes='/all_notes/' + title_of_notes + classroom_code + '.pdf'
        prod.save()
        
        return HttpResponse("Success")

    @csrf_exempt
    def doc_postSave(request):
        title_of_notes=request.POST.get('title_of_notes')
        classroom_code=request.POST.get('classroom_code')
        prod=Notes()
        prod.teachers_userName_id=request.POST.get('teacher_userName')
        prod.classroom_code_id=classroom_code
        prod.title_of_notes=title_of_notes
        prod.type=request.POST.get('type')
        prod.decpriction_of_notes=request.POST.get('decpriction_of_notes')
        notes=request.POST['notes'],
        print(notes[0])
        notesdata = base64.b64decode(notes[0])
        print(title_of_notes)
        path = settings.MEDIA_ROOT + '/all_notes/' + title_of_notes + classroom_code + '.doc'
        print(path)
        with open(path, 'wb') as f:
            f.write(notesdata)
        prod.notes='/all_notes/' + title_of_notes + classroom_code + '.doc'
        prod.save()
        
        return HttpResponse("Success")

    @csrf_exempt
    def docx_postSave(request):
        title_of_notes=request.POST.get('title_of_notes')
        classroom_code=request.POST.get('classroom_code')
        prod=Notes()
        prod.teachers_userName_id=request.POST.get('teacher_userName')
        prod.classroom_code_id=classroom_code
        prod.title_of_notes=title_of_notes
        prod.type=request.POST.get('type')
        prod.decpriction_of_notes=request.POST.get('decpriction_of_notes')
        notes=request.POST['notes'],
        print(notes[0])
        notesdata = base64.b64decode(notes[0])
        print(title_of_notes)
        path = settings.MEDIA_ROOT + '/all_notes/' + title_of_notes + classroom_code + '.docx'
        print(path)
        with open(path, 'wb') as f:
            f.write(notesdata)
        prod.notes='/all_notes/' + title_of_notes + classroom_code + '.docx'
        prod.save()
        
        return HttpResponse("Success")


    @csrf_exempt
    def mp3postSave(request):
        title_of_notes=request.POST.get('title_of_notes')
        classroom_code=request.POST.get('classroom_code')
        prod=Notes()
        prod.teachers_userName_id=request.POST.get('teacher_userName')
        prod.classroom_code_id=classroom_code
        prod.title_of_notes=title_of_notes
        prod.type='Audio'
        prod.decpriction_of_notes=request.POST.get('decpriction_of_notes')
        notes=request.POST['notes'],
        print(notes[0])
        notesdata = base64.b64decode(notes[0])
        print(title_of_notes)
        path = settings.MEDIA_ROOT + '/all_notes/' + title_of_notes + classroom_code + '.mp3'
        print(path)
        with open(path, 'wb') as f:
            f.write(notesdata)
        prod.notes='/all_notes/' + title_of_notes + classroom_code + '.mp3'
        prod.save()
        
        return HttpResponse("Success")

    # Getting  Notes from database 
    @csrf_exempt
    def NotesQuestionPapersDetails(request):
        teachers_userName = request.POST.get('teachers_userName')
        classroom_code=request.POST.get('classroom_code')
        print(teachers_userName)
        NotesDetails1=Notes.objects.filter(teachers_userName = teachers_userName, classroom_code = classroom_code, type = 'Question Paper').all()
        serializer = NotesDetailsSerializer(NotesDetails1, many = True)
        total_NotesDetails1 = json.dumps(serializer.data)
        total_NotesDetails = json.loads(total_NotesDetails1)
        data = {'Notes':total_NotesDetails}
        return JsonResponse(data)
        

    # Getting  Notes from database 
    @csrf_exempt
    def NotesDetails(request):
        teachers_userName = request.POST.get('teachers_userName')
        classroom_code=request.POST.get('classroom_code')
        print(teachers_userName)
        NotesDetails1=Notes.objects.filter(teachers_userName = teachers_userName, classroom_code = classroom_code, type = 'Notes').all()
        serializer = NotesDetailsSerializer(NotesDetails1, many = True)
        total_NotesDetails1 = json.dumps(serializer.data)
        total_NotesDetails = json.loads(total_NotesDetails1)
        data = {'Notes':total_NotesDetails}
        return JsonResponse(data)

   
    @csrf_exempt
    def AudioNotesDetails(request):
        teachers_userName = request.POST.get('teachers_userName')
        classroom_code=request.POST.get('classroom_code')
        print(teachers_userName)
        NotesDetails1=Notes.objects.filter(teachers_userName = teachers_userName, classroom_code = classroom_code, type = 'Audio').all()
        serializer = NotesDetailsSerializer(NotesDetails1, many = True)
        total_NotesDetails1 = json.dumps(serializer.data)
        total_NotesDetails = json.loads(total_NotesDetails1)
        data = {'Notes':total_NotesDetails}
        return JsonResponse(data)
