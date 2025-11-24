"""
URL configuration for student_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.shortcuts import render

def frontend_view(request):
    """Render the frontend dashboard"""
    return render(request, 'index.html')

def api_home(request):
    """API documentation endpoint"""
    return JsonResponse({
        'message': 'Welcome to Student Management API',
        'version': '1.0',
        'frontend': '/',
        'endpoints': {
            'students': '/students/',
            'get_all': 'GET /students/',
            'get_one': 'GET /students/{roll_no}/',
            'create': 'POST /students/',
            'update': 'PUT/PATCH /students/{roll_no}/',
            'delete': 'DELETE /students/{roll_no}/',
        },
        'documentation': 'See README.md for full documentation'
    })

urlpatterns = [
    path('', frontend_view, name='frontend'),
    path('api/', api_home, name='api_home'),
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
]
