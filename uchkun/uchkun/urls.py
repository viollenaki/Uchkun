from django.contrib import admin
from django.urls import path, include
from security.views import login,student_dashboard,professor_dashboard,admin_dashboard
from university.views import students

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('security/', include('security.urls')), 
     path('student-dashboard/', student_dashboard, name='student_dashboard'),
     path('',login,name="login"),
      path('professor-dashboard/', professor_dashboard, name='professor_dashboard'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),  #
    path('university/', include('university.urls')),
    path('students/', students, name='students'),

]

