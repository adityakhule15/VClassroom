from Attendence.models import ClassroomDetails
from rest_framework import serializers
from Teachers.serializers import TeacherDetailsSerializer

''' Taking Executive Login Details '''
class OnlyClassroomDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomDetails
        fields = '__all__'

class ClassroomDetailsSerializer(serializers.ModelSerializer):
    teacher_userName = TeacherDetailsSerializer()
    
    class Meta:
        model = ClassroomDetails
        fields = '__all__'




