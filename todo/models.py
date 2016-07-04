from django.db import models


class Task(models.Model):
    #author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
