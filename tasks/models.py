from django.db import models
from django.conf import settings
from projects.models import Project

class Task(models.Model):

    STATUS_CHOICES = (
        ('todo', 'Todo'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='todo'
    )

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    due_date = models.DateField()

    def __str__(self):
        return self.title