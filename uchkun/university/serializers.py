from rest_framework import serializers
from .models import Student, Professor, Subject, RegisteredSubject

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class RegisteredSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredSubject
        fields = '__all__'

    def validate_grade(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Grade must be between 0 and 100")
        return value
