from django.db import models
from django.utils import timezone


class Task(models.Model):
    #author = models.ForeignKey('auth.User')
    title = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    due_date = models.DateTimeField(
            blank=True, null=True)

    def __str__(self):
        return self.title
