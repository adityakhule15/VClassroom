from Attendence.models import QuizResult
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import QuizResultDetailsSerializer

 
@csrf_exempt
class QuizResultDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        prod=QuizResult()
        prod.quiz_id_id=request.POST.get('quiz_id')
        prod.student_userName_id=request.POST.get('student_userName')
        prod.teachers_userName_id=request.POST.get('teacher_userName')
        prod.classroom_code_id=request.POST.get('classroom_code')
        prod.obtained_marks=request.POST.get('obtained_marks')
        prod.totalMarks=request.POST.get('totalMarks')
        prod.save()
        return HttpResponse("Success")
        

    # Getting  College Details from database 
    @csrf_exempt
    def QuizResultDetails(request):
        quiz_id=request.POST.get('quiz_id')
        print(quiz_id)
        Attendence1=QuizResult.objects.filter(quiz_id=quiz_id).all()
        serializer = QuizResultDetailsSerializer(Attendence1, many = True)
        total_Attendence1 = json.dumps(serializer.data)
        total_Attendence = json.loads(total_Attendence1)
        data = {'Results':total_Attendence}
        return JsonResponse(data)

    # Getting  College Details from database 
    @csrf_exempt
    def QuizResult(request):
        quiz_id=request.POST.get('quiz_id')
        student_userName=request.POST.get('student_userName')
        print(quiz_id)
        Attendence1=QuizResult.objects.filter(quiz_id=quiz_id, student_userName = student_userName).all()
        serializer = QuizResultDetailsSerializer(Attendence1, many = True)
        total_Attendence1 = json.dumps(serializer.data)
        total_Attendence = json.loads(total_Attendence1)
        data = {'Results':total_Attendence}
        return JsonResponse(data)

