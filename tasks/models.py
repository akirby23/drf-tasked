from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from prioritylevels.models import PriorityLevel


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    priority_level = models.ForeignKey(PriorityLevel, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    task_detail = models.TextField(max_length=500)
    assignee = models.ForeignKey(
        User, on_delete=models.SET_NULL, 
        null=True, 
        related_name='assignee'
        )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Task {self.id}: {self.title}'
