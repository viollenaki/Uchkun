from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'security/login.html')


def cehack(request):
    




def main_page(request):

    return render(request, 'university/main.html')

def dashboard(request):
    """Панель управления"""
    return render(request, 'security/dashboard.html')

def profile(request):
    """Страница профиля пользователя"""
    return render(request, 'security/profile.html')

def students(request):
    return render(request, 'university/students.html')
