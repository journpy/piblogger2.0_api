from rest_framework import serializers

from users.models import CustomUser
from posts.models import Post


class CustomUserSerializer(serializers.ModelSerializer):
    """Serializer for a Custom user object."""
    class Meta:
        model = CustomUser
        fields = [
            'id', 'first_name', 'last_name', 'email', 'date_of_birth'
            ]


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post object."""
    class Meta:
        model = Post
        fields = [
            'id', 'author', 'title', 'body', 'created_at', 'modified_at', 'slug'
            ]