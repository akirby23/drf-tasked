from django.db import models

PRIORITY_LEVELS = [
    ('HIGH', 'High'),
    ('MEDIUM', 'Medium'),
    ('LOW', 'Low'),
]

class PriorityLevel(models.Model):
    name = models.CharField(
        max_length=10,
        choices = PRIORITY_LEVELS, 
        default='LOW'
    )
