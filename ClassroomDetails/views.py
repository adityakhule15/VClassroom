from Attendence.models import ClassAccess, ClassroomDetails
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt

from Students.serializers import ClassroomDetailsWithStudentSerializer
from .serializers import ClassroomDetailsSerializer

 
@csrf_exempt
class ClassroomDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        prod=ClassroomDetails()
        prod.classroom_code=request.POST.get('classroom_code')
        prod.teacher_userName_id=request.POST.get('teacher_userName')
        prod.subject_name=request.POST.get('subject_name')
        prod.date_of_creation=request.POST.get('date_of_creation')
        prod.description=request.POST.get('description')
        prod.save()
        return HttpResponse("Success")

    # Getting  College Details from database 
    @csrf_exempt
    def ClassroomDetail(request):
        classroom_code=request.POST.get('classroom_code')
        print(classroom_code)
        Attendence1=ClassroomDetails.objects.filter(classroom_code=classroom_code).all()
        serializer = ClassroomDetailsSerializer(Attendence1, many = True)
        total_Attendence1 = json.dumps(serializer.data)
        total_Attendence = json.loads(total_Attendence1)
        data = {'ClassroomDetails':total_Attendence}
        return JsonResponse(data)

    @csrf_exempt
    def ClassroomAccessTeachers(request):
        teacher_userName=request.POST.get('teacher_userName')
        print(teacher_userName)
        Attendence1=ClassroomDetails.objects.filter(teacher_userName=teacher_userName).all()
        serializer = ClassroomDetailsSerializer(Attendence1, many = True)
        total_Attendence1 = json.dumps(serializer.data)
        total_Attendence = json.loads(total_Attendence1)
        data = {'ClassroomAccessTeacher':total_Attendence}
        return JsonResponse(data)

    # Getting  College Details from database 
    @csrf_exempt
    def ClassroomAccessDetail(request):
        classroom_code=request.POST.get('classroom_code')
        print(classroom_code)
        Attendence1=ClassAccess.objects.filter(classroom_code=classroom_code).all()
        serializer = ClassroomDetailsWithStudentSerializer(Attendence1, many = True)
        total_Attendence1 = json.dumps(serializer.data)
        total_Attendence = json.loads(total_Attendence1)
        data = {'ClassroomAccessDetails':total_Attendence}
        return JsonResponse(data)