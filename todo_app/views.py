

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Note # Assuming Note is defined in models.py

# --- Note Management Views ---

class NoteList(LoginRequiredMixin, ListView):
    """
    Displays a list of all notes belonging to the currently logged-in user.
    """
    model = Note
    context_object_name = 'notes'
    template_name = 'todo_app/note_list.html'

    def get_context_data(self, **kwargs):
        """
        Ensures only the user's notes are displayed.
        """
        context = super().get_context_data(**kwargs)
        # Filter notes to only show the ones owned by the request user, ordered by creation date
        context['notes'] = context['notes'].filter(user=self.request.user).order_by('-created_at')
        return context

class NoteDetail(LoginRequiredMixin, DetailView):
    """
    Displays the details of a single note.
    """
    model = Note
    context_object_name = 'note'
    template_name = 'todo_app/note_detail.html'

    def get_queryset(self):
        """
        Ensures a user can only view their own notes.
        """
        return self.model.objects.filter(user=self.request.user)

class NoteCreate(LoginRequiredMixin, CreateView):
    """
    Handles the creation of a new note.
    """
    model = Note
    fields = ['title', 'content'] # Fields to be displayed in the form
    template_name = 'todo_app/note_form.html'
    success_url = reverse_lazy('notes') # Redirect to the notes list upon successful creation

    def form_valid(self, form):
        """
        Automatically sets the user field to the logged-in user before saving.
        """
        form.instance.user = self.request.user
        return super(NoteCreate, self).form_valid(form)

class NoteUpdate(LoginRequiredMixin, UpdateView):
    """
    Handles the updating of an existing note.
    """
    model = Note
    fields = ['title', 'content']
    template_name = 'todo_app/note_form.html'
    success_url = reverse_lazy('notes')

    def get_queryset(self):
        """
        Ensures a user can only update their own notes.
        """
        return self.model.objects.filter(user=self.request.user)

class NoteDelete(LoginRequiredMixin, DeleteView):
    """
    Handles the deletion of a note.
    """
    model = Note
    context_object_name = 'note'
    template_name = 'todo_app/note_delete.html'
    success_url = reverse_lazy('notes')

    def get_queryset(self):
        """
        Ensures a user can only delete their own notes.
        """
        return self.model.objects.filter(user=self.request.user)