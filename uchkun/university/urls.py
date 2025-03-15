from django.urls import path
from .views import StudentAPIView, ProfessorAPIView, StudentSubjectsAPIView, SubjectAPIView, RegisteredSubjectAPIView

urlpatterns = [
path('students/', StudentAPIView.as_view(), name='api_students'),
    path('professors/', ProfessorAPIView.as_view(), name='api_professors'),
    path('subjects/', SubjectAPIView.as_view(), name='api_subjects'),
    path('registered-subjects/', RegisteredSubjectAPIView.as_view(), name='api_registered_subjects'),
    path('student/subjects/', StudentSubjectsAPIView.as_view(), name='api_student_subjects')
]