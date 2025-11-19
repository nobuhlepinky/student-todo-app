

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone # Used for setting default date/time values

class Task(models.Model):
    """
    Model representing a single academic task or to-do item.
    """
    # Links the Task to a specific User. 
    # If the User is deleted, their tasks are also deleted (CASCADE).
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    # Title of the task (e.g., "History Essay," "Math Homework")
    title = models.CharField(max_length=200)
    
    # Detailed description of the task
    description = models.TextField(blank=True, null=True)
    
    # The date the task is due.
    due_date = models.DateField()
    
    # Boolean to track if the task is finished. Defaults to False (pending).
    is_completed = models.BooleanField(default=False)
    
    # Automatic timestamp for when the task was created.
    created_at = models.DateTimeField(default=timezone.now) 

    class Meta:
        # Orders tasks by due date (oldest first) by default.
        ordering = ['due_date']

    def __str__(self):
        """Returns the title of the task for easy identification in the admin."""
        return self.title

class Note(models.Model):
    """
    Model representing a structured study note or reference item.
    """
    # Links the Note to a specific User.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Title of the note (e.g., "Chapter 3 Summary," "Photosynthesis Process")
    title = models.CharField(max_length=200)
    
    # Detailed content of the note.
    content = models.TextField()
    
    # Automatic timestamp for when the note was created.
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        # Orders notes by creation date (newest first).
        ordering = ['-created_at'] 
        
    def __str__(self):
        """Returns the title of the note."""
        return self.title
