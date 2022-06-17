from Attendence.models import QuizResult
from rest_framework import serializers
from Quiz.serializers import QuizSerializer
from Students.serializers import OnlyStudentDetailsSerializer

''' Taking Executive Login Details '''
class QuizResultDetailsSerializer(serializers.ModelSerializer):
    student_userName = OnlyStudentDetailsSerializer()
    quiz_id = QuizSerializer()

    class Meta:
        model = QuizResult
        fields = '__all__'

