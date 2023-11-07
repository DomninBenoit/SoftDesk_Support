from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .serializers import IssuesSerializers
from .models import Issue
from common.permissions import IsAuthorOrContributor
from projects.models import Project


class IssuesViewSet(ModelViewSet):
    serializer_class = IssuesSerializers
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrContributor]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Issue.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project = Project.objects.get(id=self.kwargs['project_id'])
        serializer.save(project=project, assigned_to=self.request.user)


