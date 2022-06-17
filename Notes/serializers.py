from Attendence.models import Notes
from rest_framework import serializers


class NotesDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'