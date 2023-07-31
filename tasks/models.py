from django.db import models


# Create your models here.
class Tasks(models.Model):
    # User Selection Of Status

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    due_date = models.DateTimeField()
    urgency = models.BooleanField(default=False)

    def __str__(self):
        return self.title
