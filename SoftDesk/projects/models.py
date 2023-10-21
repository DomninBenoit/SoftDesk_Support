from django.db import models
from authentication.models import User
from .choices import TYPE_CHOICES


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    contributors = models.ManyToManyField(User)
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=TYPE_CHOICES.BACKEND)
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
