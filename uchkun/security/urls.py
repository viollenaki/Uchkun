from django.urls import path
from . import views

app_name = 'security'

urlpatterns = [
    path('', views.login, name='login'),  # Это страница входа - изменил name с 'main_page' на 'login'
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('main/', views.main_page, name='main_page'),
    path('students/', views.students, name='students'),
]
