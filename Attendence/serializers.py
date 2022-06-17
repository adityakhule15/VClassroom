from .models import Attendence
from rest_framework import serializers
from Teachers.serializers import TeacherDetailsSerializer

''' Taking Executive Login Details '''
class OnlyAttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = '__all__'


class AttendenceSerializer(serializers.ModelSerializer):
    teachers_userName = TeacherDetailsSerializer()
    class Meta:
        model = Attendence
        fields = '__all__'


class AttendenceDateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Attendence
        fields = 'date','classroom_code'
