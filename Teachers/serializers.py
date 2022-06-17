from Attendence.models import TeachersDetails
from rest_framework import serializers


class TeacherDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachersDetails
        fields = '__all__'