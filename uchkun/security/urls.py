from django.urls import path
from .views import RegisterView, LoginView
from . import views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Register endpoint
    path('login/', LoginView.as_view(), name='login'),  # Login endpoint
    path('', views.login, name='login'),
    path('student-dashboard/', views.student_dashboard, name='student-dashboard'),
    path('professor-dashboard/', views.professor_dashboard, name='professor-dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard')
]
