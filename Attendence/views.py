from matplotlib import dates
from .models import Attendence
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import AttendenceDateSerializer, OnlyAttendenceSerializer

 
@csrf_exempt
class AttendenceDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        prod=Attendence()
        prod.teachers_userName_id=request.POST.get('teachers_userName')
        prod.date=request.POST.get('date')
        prod.classroom_code_id=request.POST.get('classroom_code')
        prod.students_names=request.POST.get('students_names')
        prod.status=request.POST.get('status')
        prod.save()

        return HttpResponse("Success")
        
    # Getting  College Details from database 
    @csrf_exempt
    def AttendenceDetails(request):
        date=request.POST.get('date')
        classroom_code=request.POST.get('classroom_code')
        print(date)
        Attendence1=Attendence.objects.filter(date = date, classroom_code=classroom_code).all()
        serializer = OnlyAttendenceSerializer(Attendence1, many = True)
        total_Attendence1 = json.dumps(serializer.data)
        total_Attendence = json.loads(total_Attendence1)
        data = {'AttendenceDetails':total_Attendence}
        return JsonResponse(data)

    @csrf_exempt
    def AttendenceDates(request):
        teachers_userName=request.POST.get('teachers_userName')
        classroom_code=request.POST.get('classroom_code')
        print(teachers_userName)
        Attendence1=Attendence.objects.filter(teachers_userName = teachers_userName, classroom_code=classroom_code).all()
        serializer = AttendenceDateSerializer(Attendence1, many = True)
        total_Attendence1 = json.dumps(serializer.data)
        total_Attendence = json.loads(total_Attendence1)
        dates=[] # Counting in which stage how many persons present
        #Loop for counting 
        for data_ in total_Attendence:
            stage = data_['date']
            if (stage not in dates):
                dates.append(stage) 
                print(dates)            

        print(dates)
        data = {'AttendenceDates':dates}
        return JsonResponse(data)
  
    