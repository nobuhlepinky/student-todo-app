
from django import forms
from .models import Note, Task

# Base CSS classes for Tailwind styling consistency
INPUT_CLASSES = (
    'w-full p-3 border border-gray-300 rounded-lg shadow-sm '
    'focus:ring-primary focus:border-primary transition duration-150'
)

class NoteForm(forms.ModelForm):
    """
    Form for creating and updating Study Notes.
    """
    class Meta:
        model = Note
        # We only need 'title' and 'content' from the user.
        # 'user', 'created_at', and 'updated_at' are handled automatically.
        fields = ['title', 'content']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'The title of your study note or idea'
            }),
            'content': forms.Textarea(attrs={
                'class': f"{INPUT_CLASSES} h-64 resize-y",
                'placeholder': 'Type your detailed notes here...',
                'rows': 10
            }),
        }
        
        labels = {
            'title': 'Note Title',
            'content': 'Note Content',
        }

class TaskForm(forms.ModelForm):
    """
    Form for creating and updating To-Do Tasks.
    """
    class Meta:
        model = Task
        # We allow users to set the title, description, and completion status.
        fields = ['title', 'description', 'completed']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'e.g., Finish Django views'
            }),
            'description': forms.Textarea(attrs={
                'class': f"{INPUT_CLASSES} h-24 resize-y",
                'placeholder': 'Add optional details about the task...',
                'rows': 3
            }),
            'completed': forms.CheckboxInput(attrs={
                # Tailwind classes for the checkbox itself
                'class': 'h-5 w-5 text-primary border-gray-300 rounded focus:ring-primary'
            }),
        }

        labels = {
            'title': 'Task Title',
            'description': 'Task Description',
            'completed': 'Mark as Completed',
        }