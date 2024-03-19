from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

    class Meta:
        ordering = ['-name']
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"