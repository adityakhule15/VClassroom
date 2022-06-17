from Attendence.models import Login, StudentDetails, ClassAccess
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
import os
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt 
import base64
from django.conf import settings
from .serializers import OnlyStudentDetailsSerializer, StudentClassAccessDetailsSerializer

 
@csrf_exempt
class StudentDetailsList(APIView):
    # Defining the function for posting College Details

    @csrf_exempt
    def postSave(request):
        usname = request.POST.get('student_userName')
        # Saving information into login details table
        frProd = Login()
        frProd.userName= usname
        frProd.position_student = 'True'
        #  Getting the password and doing incruption of it
        sha_salt = os.urandom(32)
        frProd.salt = sha_salt
        new_key = hashlib.pbkdf2_hmac('sha256', request.POST.get('password').encode('utf-8'), bytes(str(sha_salt), 'utf-8'), 100000)
        frProd.password= new_key
        frProd.save()

        # Saving information into College details table
        prod=StudentDetails()
        prod.student_userName_id=usname
        prod.student_name=request.POST.get('student_name')
        prod.student_email=request.POST.get('student_email')
        prod.student_mobileNumber=request.POST.get('student_mobileNumber')
        prod.student_gender=request.POST.get('student_gender')
        image=request.POST['image'],
        print(image[0])
        imgdata = base64.b64decode(image[0])
        print(usname)
        path = settings.MEDIA_ROOT + '/student_images/' + usname + '.jpeg'
        print(path)
        with open(path, 'wb') as f:
            f.write(imgdata)
        prod.student_image='/student_images/' + usname + '.jpeg'
        prod.save()
       
        return HttpResponse("Success")
        
    # Getting  College Details from database 
    @csrf_exempt
    def StudentDetails(request):
        student_userName = request.POST.get('student_userName')
        print(student_userName)
        StudentDetails1=StudentDetails.objects.filter(student_userName = student_userName).all()
        serializer = OnlyStudentDetailsSerializer(StudentDetails1, many = True)
        total_StudentDetails1 = json.dumps(serializer.data)
        total_StudentDetails = json.loads(total_StudentDetails1)
        data = {'StudentDetails':total_StudentDetails}
        return JsonResponse(data)
  
    @csrf_exempt
    def update(request):       

        StudentDetails.objects.filter(student_userName = request.POST.get('student_userName')).update(
        student_name=request.POST.get('student_name'),
        student_email=request.POST.get('student_email'),
        student_mobileNumber=request.POST.get('student_mobileNumber'),
        student_gender=request.POST.get('student_gender'),
        )
        
        return HttpResponse("Success")    

    @csrf_exempt
    def updateImage(request):
    
        usname=request.POST.get('student_userName')
        print(usname)
        image=request.POST['image'],
        imgdata = base64.b64decode(image[0])
        path = settings.MEDIA_ROOT + '/student_images/' + usname + '.jpeg'
        print(path)
        with open(path, 'wb') as f:
            f.write(imgdata)
        return HttpResponse("Success")  

@csrf_exempt
class ClassroomAccess(APIView):

    @csrf_exempt
    def postClassAccess(request):
        # Saving information into College details table
        prod=ClassAccess()
        prod.student_userName_id=request.POST.get('student_userName')
        prod.classroom_code_id=request.POST.get('classroom_code')
        prod.date=request.POST.get('date')
        prod.save()
        print("Success")
        return HttpResponse("Success")


    @csrf_exempt
    def StudentClassAccessDetails(request):
        student_userName = request.POST.get('student_userName')
        print(student_userName)
        StudentDetails1=ClassAccess.objects.filter(student_userName = student_userName).all()
        serializer = StudentClassAccessDetailsSerializer(StudentDetails1, many = True)
        total_StudentDetails1 = json.dumps(serializer.data)
        total_StudentDetails = json.loads(total_StudentDetails1)
        data = {'StudentClasses':total_StudentDetails}
        return JsonResponse(data)

    @csrf_exempt
    def deleteAccess(request):
        student_userName = request.POST.get('student_userName')
        print(student_userName)
        ClassAccess.objects.filter(student_userName = student_userName).delete()
        return HttpResponse("Success")
        
