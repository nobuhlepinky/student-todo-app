

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect

from .models import Note, Task
from .forms import NoteForm, TaskForm


# --- Access Mixins ---

class BaseAccessMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Base mixin that ensures the user is logged in and is the owner
    of the object being accessed (for Detail, Update, and Delete views).
    """
    # The default redirect URL if login is required
    login_url = '/accounts/login/' 

    def test_func(self):
        """Checks if the logged-in user is the owner of the object."""
        obj = self.get_object()
        # For new objects (CreateView), this check is not needed, 
        # but for existing objects, ensure the object belongs to the user.
        return obj.user == self.request.user

    # Overriding to handle CreateView case where there is no object yet
    def get_object(self, queryset=None):
        if self.kwargs.get(self.pk_url_kwarg) is None and isinstance(self, CreateView):
            # Allow creation views to pass without failing on test_func
            return True 
        return super().get_object(queryset)

    
# --- General View ---

def index(request):
    """
    The main index page of the application.
    """
    # Render the dashboard as the index page (dashboard template is at templates/dashboard.html)
    return render(request, 'dashboard.html', {'title': 'Home'})


# ----------------------------------
#          NOTE VIEWS
# ----------------------------------

class NoteListView(LoginRequiredMixin, ListView):
    """
    Displays a list of all notes belonging to the current user.
    """
    model = Note
    template_name = 'todo_app/note_list.html'
    context_object_name = 'notes'
    
    def get_queryset(self):
        # Filter notes to show only those created by the logged-in user
        return Note.objects.filter(user=self.request.user).order_by('-updated_at')

class NoteDetailView(BaseAccessMixin, DetailView):
    """
    Displays the details of a single note. Requires login and ownership.
    """
    model = Note
    template_name = 'todo_app/note_detail.html'
    context_object_name = 'note'
    
class NoteCreateView(LoginRequiredMixin, CreateView):
    """
    Handles the creation of a new note. Requires login.
    """
    model = Note
    form_class = NoteForm
    template_name = 'todo_app/note_form.html'
    
    def form_valid(self, form):
        # Automatically set the user before saving the form
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        # Redirect to the detail page of the newly created note
        return reverse_lazy('note_app:note_detail', kwargs={'pk': self.object.pk})
        
class NoteUpdateView(BaseAccessMixin, UpdateView):
    """
    Handles updating an existing note. Requires login and ownership.
    """
    model = Note
    form_class = NoteForm
    template_name = 'todo_app/note_form.html'
    
    def get_success_url(self):
        # Redirect back to the detail page after updating
        return reverse_lazy('note_app:note_detail', kwargs={'pk': self.object.pk})

class NoteDeleteView(BaseAccessMixin, DeleteView):
    """
    Handles the deletion of a note. Requires login and ownership.
    """
    model = Note
    template_name = 'todo_app/note_confirm_delete.html'
    # Redirect to the note list after successful deletion
    success_url = reverse_lazy('note_app:note_list')


# ----------------------------------
#          TASK VIEWS
# ----------------------------------

class TaskListView(LoginRequiredMixin, ListView):
    """
    Displays a list of all tasks belonging to the current user.
    """
    model = Task
    template_name = 'todo_app/task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        # Filter tasks to show only those created by the logged-in user
        return Task.objects.filter(user=self.request.user).order_by('completed', '-created_at')

class TaskCreateView(LoginRequiredMixin, CreateView):
    """
    Handles the creation of a new task. Requires login.
    """
    model = Task
    form_class = TaskForm
    template_name = 'todo_app/task_form.html'
    success_url = reverse_lazy('note_app:task_list') # Redirect to the task list after creation

    def form_valid(self, form):
        # Automatically set the user before saving the form
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class TaskUpdateView(BaseAccessMixin, UpdateView):
    """
    Handles updating an existing task. Requires login and ownership.
    """
    model = Task
    form_class = TaskForm
    template_name = 'todo_app/task_form.html'
    success_url = reverse_lazy('note_app:task_list') # Redirect to the task list after updating

class TaskDeleteView(BaseAccessMixin, DeleteView):
    """
    Handles the deletion of a task. Requires login and ownership.
    """
    model = Task
    template_name = 'todo_app/task_confirm_delete.html'
    # Redirect to the task list after successful deletion
    success_url = reverse_lazy('note_app:task_list')


@login_required
def task_toggle_complete(request, pk):
    """
    Function-based view to toggle the 'completed' status of a task.
    """
    # Get the task or return a 404 error
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    # Check ownership explicitly just in case the get_object_or_404 fails to filter
    if task.user != request.user:
        # Should be caught by get_object_or_404, but good practice
        return redirect('note_app:task_list')

    # Toggle the status
    task.completed = not task.completed
    task.save()
    
    # Redirect the user back to the task list view
    return HttpResponseRedirect(reverse_lazy('note_app:task_list'))