from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password, make_password
from .models import User
from .serializers import UserSerializer

# Register View using DRF APIView
class RegisterView(APIView):
    def post(self, request):
        # Data received from request body
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user_type = data.get('user_type', 'student')  # Default to 'student' if not provided

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create and save the new user
        hashed_password = make_password(password)  # Hash the password before saving
        new_user = User.objects.create(
            username=username,
            password=hashed_password,
            user_type=user_type
        )
        return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)

# Login View using DRF APIView
class LoginView(APIView):
    def post(self, request):
        # Data received from request body
        data = request.data
        username = data.get('username')
        password = data.get('password')

        # Check if the user exists
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Check if the password is correct
        if check_password(password, user.password):
            return Response({'message': 'Login successful.', 'user_type': user.user_type})
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
from django.shortcuts import render

def admin_dashboard(request):
    return render(request, 'university/main.html')

def professor_dashboard(request):
    return render(request, 'teachers/professor.html')

def student_dashboard(request):
    return render(request, 'student/student-dashboard.html')
def login(request):
    return render(request, 'security/login.html')