from django.db import models
from projects.models import Project
from authentication.models import User
from .choices import PRIORITY_CHOICES, LABEL_CHOICES, STATUS_CHOICES


class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=STATUS_CHOICES.TODO)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, default=PRIORITY_CHOICES.LOW)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.PositiveSmallIntegerField(choices=LABEL_CHOICES, default=LABEL_CHOICES.BUG)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
