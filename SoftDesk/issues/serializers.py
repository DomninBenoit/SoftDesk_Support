from rest_framework import serializers
from .models import Issue


class IssuesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'status', 'priority', 'assigned_to', 'label', 'project']
        read_only_fields = ('assigned_to', 'project')

    def create(self, validated_data):
        validated_data["assigned_to"] = self.context["request"].user
        return super().create(validated_data)
