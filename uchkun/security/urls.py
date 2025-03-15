from django.urls import path
from .views import RegisterView, LoginView,student_dashboard,professor_dashboard,admin_dashboard,login

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Register endpoint
    path('login/', LoginView.as_view(), name='login'),
]
