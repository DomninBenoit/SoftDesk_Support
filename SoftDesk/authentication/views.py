from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework import permissions

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ManageUserView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Retourne l'utilisateur authentifié
        return self.request.user


