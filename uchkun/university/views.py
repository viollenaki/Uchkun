from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password, make_password
from .serializers import StudentSerializer, ProfessorSerializer, SubjectSerializer, RegisteredSubjectSerializer
from .models import Student, Professor, Subject, RegisteredSubject


# Create your views here.

# API Views for Student model
class StudentAPIView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

# API Views for Professor model
class ProfessorAPIView(APIView):
    def post(self, request):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        professors = Professor.objects.all()
        serializer = ProfessorSerializer(professors, many=True)
        return Response(serializer.data)

# API Views for Subject model
class SubjectAPIView(APIView):
    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

# API Views для модели RegisteredSubject
class RegisteredSubjectAPIView(APIView):
    def post(self, request):
        serializer = RegisteredSubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        registered_subjects = RegisteredSubject.objects.all()
        serializer = RegisteredSubjectSerializer(registered_subjects, many=True)
        return Response(serializer.data)

# API View для получения зарегистрированных предметов конкретного студента
class StudentSubjectsAPIView(APIView):
    def get(self, request):
        try:
            # Фильтруем по имени студента, а не по ID
            student_name = request.GET.get('student_name')
            if not student_name:
                return Response({'error': 'student_name parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

            registered_subjects = RegisteredSubject.objects.filter(student_name=student_name)
            serializer = RegisteredSubjectSerializer(registered_subjects, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
def students(request):
    return render(request, 'university/students.html')