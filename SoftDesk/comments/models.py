from django.db import models
from issues.models import Issue
from authentication.models import User


class Comment(models.Model):
    text = models.TextField()
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
