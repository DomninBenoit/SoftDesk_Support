from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Project
from .serializers import ProjectSerializer
from common.permissions import IsAuthor


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthor]


    def get_queryset(self):
        return Project.objects.filter(author=self.request.user)
