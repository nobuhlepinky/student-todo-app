from django import forms
# Ensure you have 'Task' model imported here (assuming it was created in models.py)
from .models import Task 
# We'll also define the NoteForm here for the next step, 
# but for now, TaskForm is the critical fix.

class TaskForm(forms.ModelForm):
    """
    A ModelForm linked to the Task model. 
    This form is used for creating and updating tasks.
    """
    class Meta:
        # Use the Task model as the source for the form fields
        model = Task
        
        # Specify which fields from the model should be included in the form
        fields = ['title', 'description', 'due_date', 'is_completed']
        
        # Optional: Add custom styling or widgets
        widgets = {
            # Use DateInput widget to show a calendar picker for the due_date
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            # Add a class for basic styling to other fields
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
