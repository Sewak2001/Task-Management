from django.db import models
from accounts.models import CustomUser

class Task(models.Model):
    STATUS_CHOICES = [
        ('Todo', 'Todo'),
        ('Inprogress', 'Inprogress'),
        ('Done', 'Done'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Todo')
    members = models.ManyToManyField(CustomUser, related_name="tasks", null=True, blank=True)

    def __str__(self):
        return self.title
