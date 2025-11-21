from django.urls import path
from . import views

# Set the namespace for this application
app_name = 'note_app'

urlpatterns = [
    # --- General/Index Views ---
    path('', views.index, name='index'),

    # --- Note URLs (Study Notes) ---
    path('notes/', views.NoteListView.as_view(), name='note_list'),
    path('notes/create/', views.NoteCreateView.as_view(), name='note_create'),
    path('notes/<int:pk>/', views.NoteDetailView.as_view(), name='note_detail'),
    path('notes/<int:pk>/update/', views.NoteUpdateView.as_view(), name='note_update'),
    path('notes/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note_delete'),
    
    # --- Task URLs (To-Do List) ---
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
    
    # Custom view for toggling task completion status
    path('tasks/<int:pk>/toggle/', views.task_toggle_complete, name='task_toggle_complete'),
]