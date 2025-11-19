from django.urls import path
from . import views

# Set the app name for URL namespace separation (good practice)
app_name = 'todo_app'

urlpatterns = [
    # Main Dashboard (Root of the app '/')
    path('', views.dashboard, name='dashboard'),
    
    # -------------------------------------------------
    # Task Management URLs
    # -------------------------------------------------
    # R - Read (List all tasks)
    path('tasks/', views.task_list, name='task_list'),
    
    # C - Create (Add a new task)
    path('tasks/create/', views.task_create, name='task_create'),
    
    # U - Update (Edit an existing task, needs the task's ID: pk)
    path('tasks/update/<int:pk>/', views.task_update, name='task_update'),
    
    # D - Delete / Toggle Complete (Handles deleting or toggling status, needs the task's ID)
    path('tasks/delete/<int:pk>/', views.task_delete, name='task_delete'),
    
    # Note Paths will go here later:
    # path('notes/', views.note_list, name='note_list'),
]