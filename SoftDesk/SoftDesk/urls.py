"""SoftDesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.views import ProjectViewSet, ContributorsViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.views import UserCreateAPIView, ManageUserView
from issues.views import IssuesViewSet
from comments.views import CommentViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'projects/(?P<project_id>\d+)/issues', IssuesViewSet, basename='issue')
router.register(r'projects/(?P<project_id>\d+)/issues/(?P<issue_id>\d+)/comments',
                CommentViewSet, basename='comment')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/', UserCreateAPIView.as_view(), name='user-create'),
    path('api/users/me/', ManageUserView.as_view(), name='user-me'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/projects/<int:project_id>/contributors/',
         ContributorsViewSet.as_view({'post': 'post', 'get': 'get'}),
         name='project-contributors'),
    path('api/projects/<int:project_id>/contributors/<int:user_pk>/',
         ContributorsViewSet.as_view({'delete': 'delete'}),
         name='project-contributor-detail'),
]
