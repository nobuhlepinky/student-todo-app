

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, Note # <-- CRITICAL: Imports your data models
from .forms import TaskForm    # <-- CRITICAL: Imports the Task Form
from django.db.models import Count 

@login_required
def dashboard(request):
    """
    The main dashboard view. Fetches key metrics for the user to display 
    upon login. This requires the user to be logged in (@login_required).
    """
    # 1. Fetch user-specific tasks and notes
    user_tasks = Task.objects.filter(user=request.user)
    
    # 2. Calculate metrics for the cards
    total_tasks = user_tasks.count()
    completed_tasks = user_tasks.filter(is_completed=True).count()
    pending_tasks = total_tasks - completed_tasks
    
    # 3. Fetch recent notes (top 5, newest first)
    # We use a placeholder here as the Note model is created but not implemented yet.
    recent_notes = Note.objects.filter(user=request.user).order_by('-created_at')[:5]

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'recent_notes': recent_notes,
    } 
    return render(request, 'dashboard.html', context)


# --- Task Management Views (Already created) ---

@login_required
def task_list(request):
    """
    Displays a list of all tasks for the logged-in user.
    """
    tasks = Task.objects.filter(user=request.user).order_by('due_date')
    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)


@login_required
def task_create(request):
    """Handles the creation of a new Task."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todo_app:task_list')
    else:
        form = TaskForm()
        
    context = {'form': form, 'page_title': 'Add New Task'}
    return render(request, 'tasks/task_form.html', context)


@login_required
def task_update(request, pk):
    """Handles updating an existing Task."""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_app:task_list')
    else:
        form = TaskForm(instance=task)
        
    context = {'form': form, 'page_title': 'Edit Task'}
    return render(request, 'tasks/task_form.html', context)


@login_required
def task_delete(request, pk):
    """Handles deleting a task and confirms completion status update."""
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == 'POST':
        if 'toggle_complete' in request.POST:
            task.is_completed = not task.is_completed
            task.save()
            return redirect('todo_app:task_list')

        elif 'delete_task' in request.POST:
            task.delete()
            return redirect('todo_app:task_list')
    
    return redirect('todo_app:task_list')
