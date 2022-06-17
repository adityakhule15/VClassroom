from Attendence.models import QuizAccess, QuizDetails
from rest_framework import serializers
from ClassroomDetails.serializers import OnlyClassroomDetailsSerializer
from Teachers.serializers import TeacherDetailsSerializer

''' Taking Executive Login Details '''
class QuizDetailsSerializer(serializers.ModelSerializer):
    teachers_userName = TeacherDetailsSerializer()
    classroom_code = OnlyClassroomDetailsSerializer()
    
    class Meta:
        model = QuizDetails
        fields = '__all__'

class QuizAccessSerializer(serializers.ModelSerializer):    
    class Meta:
        model = QuizAccess
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):    
    class Meta:
        model = QuizDetails
        fields = 'quiz_id','date','quiz_topic'



