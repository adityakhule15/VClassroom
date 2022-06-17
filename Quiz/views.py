from datetime import date
from Attendence.models import QuizAccess, QuizDetails
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import QuizAccessSerializer, QuizDetailsSerializer, QuizSerializer

 
@csrf_exempt
class QuizDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        prod=QuizDetails()
        prod.quiz_id=request.POST.get('quiz_id')
        prod.teachers_userName_id=request.POST.get('teacher_userName')
        prod.classroom_code_id=request.POST.get('classroom_code')
        prod.date=request.POST.get('date')
        prod.totalMarks=request.POST.get('totalMarks')
        prod.quiz_topic=request.POST.get('quiz_topic')
        prod.question1=request.POST.get('question1')
        prod.answer1_option1=request.POST.get('answer1_option1')
        prod.answer1_option2=request.POST.get('answer1_option2')
        prod.answer1_option3=request.POST.get('answer1_option3')
        prod.answer1_option4=request.POST.get('answer1_option4')
        prod.correct1_answer_option=request.POST.get('correct1_answer_option')
        prod.marks1=request.POST.get('marks1')
        prod.question2=request.POST.get('question2')
        prod.answer2_option1=request.POST.get('answer2_option1')
        prod.answer2_option2=request.POST.get('answer2_option2')
        prod.answer2_option3=request.POST.get('answer2_option3')
        prod.answer2_option4=request.POST.get('answer2_option4')
        prod.correct2_answer_option=request.POST.get('correct2_answer_option')
        prod.marks2=request.POST.get('marks2')
        prod.question3=request.POST.get('question3')
        prod.answer3_option1=request.POST.get('answer3_option1')
        prod.answer3_option2=request.POST.get('answer3_option2')
        prod.answer3_option3=request.POST.get('answer3_option3')
        prod.answer3_option4=request.POST.get('answer3_option4')
        prod.correct3_answer_option=request.POST.get('correct3_answer_option')
        prod.marks3=request.POST.get('marks3')
        prod.question4=request.POST.get('question4')
        prod.answer4_option1=request.POST.get('answer4_option1')
        prod.answer4_option2=request.POST.get('answer4_option2')
        prod.answer4_option3=request.POST.get('answer4_option3')
        prod.answer4_option4=request.POST.get('answer4_option4')
        prod.correct4_answer_option=request.POST.get('correct4_answer_option')
        prod.marks4=request.POST.get('marks4')
        prod.question5=request.POST.get('question5')
        prod.answer5_option1=request.POST.get('answer5_option1')
        prod.answer5_option2=request.POST.get('answer5_option2')
        prod.answer5_option3=request.POST.get('answer5_option3')
        prod.answer5_option4=request.POST.get('answer5_option4')
        prod.correct5_answer_option=request.POST.get('correct5_answer_option')
        prod.marks5=request.POST.get('marks5')
        prod.question6=request.POST.get('question6')
        prod.answer6_option1=request.POST.get('answer6_option1')
        prod.answer6_option2=request.POST.get('answer6_option2')
        prod.answer6_option3=request.POST.get('answer6_option3')
        prod.answer6_option4=request.POST.get('answer6_option4')
        prod.correct6_answer_option=request.POST.get('correct6_answer_option')
        prod.marks6=request.POST.get('marks6')
        prod.question7=request.POST.get('question7')
        prod.answer7_option1=request.POST.get('answer7_option1')
        prod.answer7_option2=request.POST.get('answer7_option2')
        prod.answer7_option3=request.POST.get('answer7_option3')
        prod.answer7_option4=request.POST.get('answer7_option4')
        prod.correct7_answer_option=request.POST.get('correct7_answer_option')
        prod.marks7=request.POST.get('marks7')
        prod.question8=request.POST.get('question8')
        prod.answer8_option1=request.POST.get('answer8_option1')
        prod.answer8_option2=request.POST.get('answer8_option2')
        prod.answer8_option3=request.POST.get('answer8_option3')
        prod.answer8_option4=request.POST.get('answer8_option4')
        prod.correct8_answer_option=request.POST.get('correct8_answer_option')
        prod.marks8=request.POST.get('marks8')
        prod.question9=request.POST.get('question9')
        prod.answer9_option1=request.POST.get('answer9_option1')
        prod.answer9_option2=request.POST.get('answer9_option2')
        prod.answer9_option3=request.POST.get('answer9_option3')
        prod.answer9_option4=request.POST.get('answer9_option4')
        prod.correct9_answer_option=request.POST.get('correct9_answer_option')
        prod.marks9=request.POST.get('marks9')
        prod.question10=request.POST.get('question10')
        prod.answer10_option1=request.POST.get('answer10_option1')
        prod.answer10_option2=request.POST.get('answer10_option2')
        prod.answer10_option3=request.POST.get('answer10_option3')
        prod.answer10_option4=request.POST.get('answer10_option4')
        prod.correct10_answer_option=request.POST.get('correct10_answer_option')
        prod.marks10=request.POST.get('marks10')
        prod.save()
        return HttpResponse("Success")
          
    # Getting  College Details from database 
    @csrf_exempt
    def ScheduledQuiz(request):
        date1=date.today()
        classroom_code=request.POST.get('classroom_code')
        Quiz1=QuizDetails.objects.filter(date=date1, classroom_code=classroom_code).all()
        serializer = QuizDetailsSerializer(Quiz1, many = True)
        total_Quiz1 = json.dumps(serializer.data)
        total_Quiz = json.loads(total_Quiz1)
        data = {'Quiz':total_Quiz}
        print(total_Quiz)       
        return JsonResponse(data)
        
    @csrf_exempt
    def QuizDetail(request):
        quiz_id=request.POST.get('quiz_id')
        Quiz1=QuizDetails.objects.filter(quiz_id=quiz_id).all()
        serializer = QuizDetailsSerializer(Quiz1, many = True)
        total_Quiz1 = json.dumps(serializer.data)
        total_Quiz = json.loads(total_Quiz1)
        data = {'QuizDetails':total_Quiz}
        return JsonResponse(data)

    # # Getting  College Details from database 
    # @csrf_exempt
    # def QuizDetail(request):
    #     quiz_id=request.POST.get('quiz_id')
    #     print(quiz_id)
    #     id = request.POST.get('id')
    #     print(id)
    #     QuizAccess1=QuizAccess.objects.filter(id=id).all()
    #     serializer = QuizAccessSerializer(QuizAccess1, many = True)
    #     total_QuizAccess1 = json.dumps(serializer.data)
    #     total_QuizAccess = json.loads(total_QuizAccess1)
    #     if (total_QuizAccess.length == 0):
    #         print(total_QuizAccess.length)
    #         Quiz1=QuizDetails.objects.filter(quiz_id=quiz_id).all()
    #         serializer = QuizDetailsSerializer(Quiz1, many = True)
    #         total_Quiz1 = json.dumps(serializer.data)
    #         total_Quiz = json.loads(total_Quiz1)
    #         data = {'QuizDetails':total_Quiz}
    #         return JsonResponse(data)
    #     data = {'QuizDetails':total_QuizAccess}
    #     return JsonResponse(data)

    # Getting  College Details from database
    @csrf_exempt
    def QuizList(request):
        classroom_code=request.POST.get('classroom_code')
        print(classroom_code)
        Quiz1=QuizDetails.objects.filter(classroom_code=classroom_code).all()
        serializer = QuizSerializer(Quiz1, many = True)
        total_Quiz1 = json.dumps(serializer.data)
        total_Quiz = json.loads(total_Quiz1)
        data = {'QuizList':total_Quiz}
        return JsonResponse(data)

