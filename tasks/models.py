from django.db import models

# Create your models here.
class Task(models.Model):
    # User Selection Of Status
    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    )

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    urgency = models.BooleanField(default=False)