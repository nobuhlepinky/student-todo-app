from django.urls import path
from .views import (
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView
)

urlpatterns = [
    # --- Task Management URLs ---
    path('', TaskListView.as_view(), name='tasks'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),

    # --- Note Management URLs (NEW) ---
    path('notes/', NoteListView.as_view(), name='notes'),
    path('note-create/', NoteCreateView.as_view(), name='note-create'),
    path('note-update/<int:pk>/', NoteUpdateView.as_view(), name='note-update'),
    path('note-delete/<int:pk>/', NoteDeleteView.as_view(), name='note-delete'),
]