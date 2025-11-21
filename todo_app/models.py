


from django.db import models
from django.contrib.auth import get_user_model

# Get the custom or default User model for Foreign Keys
User = get_user_model()

class Note(models.Model):
    """
    Represents a study note or general memo.
    Each note belongs to a specific user.
    """
    # Foreign Key to the User model
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes',
        verbose_name='User'
    )
    
    title = models.CharField(
        max_length=200, 
        verbose_name='Title'
    )
    
    content = models.TextField(
        blank=True, 
        verbose_name='Content'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Created At'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name='Last Updated'
    )

    class Meta:
        # Order notes by date created (newest first)
        ordering = ['-created_at']
        verbose_name = 'Study Note'
        verbose_name_plural = 'Study Notes'

    def __str__(self):
        """Return a string representation of the note (its title)."""
        return self.title

class Task(models.Model):
    """
    Represents a to-do list task.
    Each task belongs to a specific user.
    """
    # Foreign Key to the User model
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='User'
    )
    
    title = models.CharField(
        max_length=255, 
        verbose_name='Task Title'
    )
    
    description = models.TextField(
        blank=True, 
        verbose_name='Description (Optional)'
    )
    
    completed = models.BooleanField(
        default=False, 
        verbose_name='Completed'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Created At'
    )

    class Meta:
        # Order tasks by completion status (incomplete first) and then by creation date
        ordering = ['completed', '-created_at']
        verbose_name = 'To-Do Task'
        verbose_name_plural = 'To-Do Tasks'
    
    def __str__(self):
        """Return a string representation of the task (its title and completion status)."""
        status = "[DONE]" if self.completed else "[TODO]"
        return f"{status} {self.title}"