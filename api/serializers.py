from rest_framework import serializers
from students.models import Student


# Model Serializer for Student model

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'