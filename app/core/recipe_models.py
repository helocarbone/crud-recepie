import uuid

from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ingredients = models.JSONField()

    def __str__(self):
        return self.name
