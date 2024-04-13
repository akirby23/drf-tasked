from django.db import models


class Category(models.Model):
    """
    For category creation
    Related to the Task model
    """
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

    class Meta:
        ordering = ['-name']
        # Verbose names added for improved readability
        # on the admin panel
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"
