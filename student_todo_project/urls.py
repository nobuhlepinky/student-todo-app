"""
URL configuration for student_todo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    # The 'todo_app/' path handles all application logic (Tasks, Notes, Dashboard)
    path('', include('todo_app.urls')),
    
    # The 'login/', 'logout/', and 'register/' paths use Django's built-in auth views
    # handled directly in the todo_app's urls.py now.
    # The main project's urls.py just includes the app's urls.
]