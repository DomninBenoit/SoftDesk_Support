from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import permissions, status
from .models import Project
from .serializers import ProjectSerializer, ContributorSerializer
from common.permissions import IsAuthorOrContributor
from authentication.serializers import UserSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrContributor]

    def get_queryset(self):
        return Project.objects.filter(author=self.request.user)


class ContributorsViewSet(ViewSet):
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrContributor]

    def get_project(self, project_id):
        return get_object_or_404(Project, id=self.kwargs['project_id'])

    def post(self, request, project_id=None,):
        project = self.get_project(project_id)
        serializer = ContributorSerializer(data=request.data, context={'project': project})
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response({'status': 'User added as contributor'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, project_id=None,):
        project = self.get_project(project_id)
        contributors = project.contributors.all()
        serializer = UserSerializer(contributors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, project_id=None, user_pk=None):
        project = self.get_project(project_id)
        serializer = ContributorSerializer(data={'user_id': user_pk}, context={'project': project})
        if serializer.is_valid():
            serializer.delete(project, serializer.validated_data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
