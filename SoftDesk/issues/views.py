from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .serializers import IssuesSerializers
from .models import Issue
from common.permissions import IsAuthorOrContributor


class IssuesViewSet(ModelViewSet):
    serializer_class = IssuesSerializers
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrContributor]

    def get_queryset(self):
        queryset = Issue.objects.all()
        project_id = self.request.query_params.get('project', None)
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset


