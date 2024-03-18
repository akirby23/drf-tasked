from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True)
    priority_level = models.ForeignKey('prioritylevels.PriorityLevel', on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=False)
    task_detail = models.TextField(max_length=500)
    assignee = models.ForeignKey(
        User, on_delete=models.SET_NULL, 
        null=True, 
        related_name='assignee'
        )

    class Meta:
        ordering = []

    def __str__(self):
        return f'{self.id} {self.title}'
