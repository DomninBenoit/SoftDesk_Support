from rest_framework import serializers
from .models import Project
from authentication.models import User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'type', 'created_time', 'author']
        read_only_fields = ('author', 'created_time')

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)


class ContributorSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    def validate_user_id(self, value):
        try:
            User.objects.get(id=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")
        return value

    def create(self, validated_data):
        user_id = validated_data.get('user_id')
        user = User.objects.get(id=user_id)
        project = self.context['project']
        if project.contributors.filter(id=user_id).exists():
            raise serializers.ValidationError("User is already a contributor")
        project.contributors.add(user)
        return project

    def delete(self, instance, validated_data):
        user_id = validated_data.get('user_id')
        user = User.objects.get(id=user_id)
        instance.contributors.remove(user)
        return instance

