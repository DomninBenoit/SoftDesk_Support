from django.core.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from .models import Project
from .serializers import ProjectSerializer, ContributorSerializer
from common.permissions import IsAuthorOrContributor
from authentication.serializers import UserSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrContributor]

    def get_queryset(self):
        return Project.objects.filter(author=self.request.user)

    @action(detail=True, methods=['post'], url_path='contributors/add')
    def add_contributor(self, request, pk=None):
        project = self.get_object()
        serializer = ContributorSerializer(data=request.data, context={'project': project})
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response({'status': 'User added as contributor'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path='contributors')
    def list_contributors(self, request, pk=None):
        project = self.get_object()
        contributors = project.contributors.all()
        serializer = UserSerializer(contributors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['delete'], url_path='contributors/(?P<user_pk>[^/.]+)')
    def remove_contributor(self, request, pk=None, user_pk=None):
        project = self.get_object()
        serializer = ContributorSerializer(data={'user_id': user_pk}, context={'project': project})
        if serializer.is_valid():
            serializer.delete(project, serializer.validated_data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
