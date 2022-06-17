from django.http.response import HttpResponse
from rest_framework.views import APIView
from Attendence.models import Login, StudentDetails, TeachersDetails
import os
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt
from Students.serializers import OnlyStudentDetailsSerializer
from Teachers.serializers import TeacherDetailsSerializer

# Create your views here
@csrf_exempt
class ForgotpasswordandCreatpassword(APIView):
    @csrf_exempt
    def creatpassword(request):
        frProd = Login()
        sha_salt = os.urandom(32)
        frProd.salt = sha_salt
        new_key = hashlib.pbkdf2_hmac('sha256', request.POST.get('password').encode('utf-8'), bytes(str(sha_salt), 'utf-8'), 100000)
        Login.objects.filter(userName = request.POST.get('userName')).update(password=new_key,salt = sha_salt)
        return HttpResponse("Success")
        
    @csrf_exempt
    def otpVerification(request):
        OTP=request.POST.get('OTP')
        print(OTP)
        if OTP == '6543':
            return HttpResponse("Success")
        return HttpResponse("Failure")

    #posting a input data for checking   
    @csrf_exempt
    def forgotpassword(request):
        userName=request.POST.get('userName')
        position=request.POST.get('position') 
        email=request.POST.get('email')
        # print("Mai aaa rha hu...................................:")

        if position == 'Teacher':
            LoginDetails1=TeachersDetails.objects.filter(teachers_userName=userName,teachers_email=email).all()
            serializer = TeacherDetailsSerializer(LoginDetails1, many = True)
            total_LoginDetails1 = json.dumps(serializer.data)
            total_LoginDetails = json.loads(total_LoginDetails1)
            if len(total_LoginDetails) > 0:
                print("Success")
                #need to call otp url
                return HttpResponse("Success")

        elif position == 'Student':
            LoginDetails1=StudentDetails.objects.filter(student_userName=userName,student_email=email).all()
            serializer = OnlyStudentDetailsSerializer(LoginDetails1, many = True)
            total_LoginDetails1 = json.dumps(serializer.data)
            total_LoginDetails = json.loads(total_LoginDetails1)
            if len(total_LoginDetails) > 0:
                print("Success")
                #need to call otp url
                return HttpResponse("Success")

        return HttpResponse("Failure")

       