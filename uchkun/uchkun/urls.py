from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('security/', include('security.urls')),  # Include the security app's urls
]

