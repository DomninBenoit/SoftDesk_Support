from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .serializers import CommentSerializer
from .models import Comment
from common.permissions import IsAuthorOrContributor
from issues.models import Issue


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrContributor]

    def get_queryset(self):
        issue_id = self.kwargs['issue_id']
        return Comment.objects.filter(issue_id=issue_id)

    def perform_create(self, serializer):
        issue = Issue.objects.get(id=self.kwargs['issue_id'])
        serializer.save(issue=issue, author=self.request.user)
