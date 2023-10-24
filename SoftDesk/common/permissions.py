from rest_framework.permissions import BasePermission


class IsAuthorOrContributor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or obj.contributors.filter(id=request.user.id).exists()
