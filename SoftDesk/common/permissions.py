from rest_framework.permissions import BasePermission, SAFE_METHODS
from projects.models import Project

class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsAuthorOrContributor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Project):
            project = obj
            user_related_field = obj.author
        elif hasattr(obj, 'assigned_to'):
            project = obj.project
            user_related_field = obj.assigned_to
        elif hasattr(obj, 'issue'):
            project = obj.issue.project
            user_related_field = obj.author
        else:
            return False

        if request.method not in SAFE_METHODS:
            return user_related_field == request.user
        return user_related_field == request.user or project.contributors.filter(id=request.user.id).exists()
