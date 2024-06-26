from django.db import models


class PriorityLevel(models.Model):
    """
    For priority level creation
    Related to the Task model
    """
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return f"{self.name}"
