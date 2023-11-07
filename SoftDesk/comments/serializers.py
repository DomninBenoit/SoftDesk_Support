from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'issue', 'author']
        read_only_fields = ('author', 'issue')

    def create(self, validated_data):
        validated_data['author'] = self.context["request"].user
        return super().create(validated_data)


