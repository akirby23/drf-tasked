from django.db import models

CATEGORY_CHOICES = [
    ('EDUCATION', 'Education'),
    ('WORK', 'Work'),
    ('HEALTH_AND_FITNESS', 'Health & Fitness'),
    ('HOBBIES', 'Hobbies'),
    ('SELF_CARE', 'Self Care'),
    ('HOME', 'Home'),
    ('SOCIAL', 'Social'),
]
class Category(models.Model):
    name = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
