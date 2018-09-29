from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    labels = models.CharField(max_length=400)
    created_by = models.ForeignKey(User, related_name='notes')

    def __str__(self):
        """A string representation of the model."""
        return self.title