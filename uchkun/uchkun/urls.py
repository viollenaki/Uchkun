from django.contrib import admin
from django.urls import path, include
from security.views import login,student_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('security/', include('security.urls')), 
     path('student-dashboard/', student_dashboard, name='student_dashboard'),
     path('',login,name="login") # Include the security app's urls
]

