from Attendence.models import ClassAccess, StudentDetails
from rest_framework import serializers
from ClassroomDetails.serializers import OnlyClassroomDetailsSerializer


class OnlyStudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__'


class StudentClassAccessDetailsSerializer(serializers.ModelSerializer):
    classroom_code = OnlyClassroomDetailsSerializer()

    class Meta:
        model = ClassAccess
        fields = '__all__'

class ClassroomDetailsWithStudentSerializer(serializers.ModelSerializer):
    student_userName = OnlyStudentDetailsSerializer()
    
    class Meta:
        model = ClassAccess
        fields = '__all__'




