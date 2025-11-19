
from django import forms
from .models import Task, Note

# --- Task Form (Existing) ---
class TaskForm(forms.ModelForm):
    """
    Form for creating and updating Task instances.
    """
    class Meta:
        model = Task
        # Fields that the user can modify on the form
        fields = ['title', 'description', 'due_date', 'is_completed']
        # Customize the input widgets for better user experience
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Task Title'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Details about the task...'}),
            'due_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
        }


# --- Note Form (NEW) ---
class NoteForm(forms.ModelForm):
    """
    Form for creating and updating Note instances.
    """
    class Meta:
        model = Note
        # Fields that the user can modify on the form
        fields = ['title', 'content']
        # Customize the input widgets
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Note Title (e.g., Chapter 3 Summary)'}),
            # Textarea for the main content, giving it a larger feel
            'content': forms.Textarea(attrs={'class': 'form-textarea large', 'placeholder': 'Start writing your notes here... (Supports Markdown)', 'rows': 15}),
        }