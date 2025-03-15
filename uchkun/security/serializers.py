from rest_framework import serializers
from ..security.models import Student, Professor, Subject, RegisteredSubject, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}

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
