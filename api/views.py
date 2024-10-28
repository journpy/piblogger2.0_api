from rest_framework import viewsets

from users.models import CustomUser
from posts.models import Post
from .serializers import CustomUserSerializer, PostSerializer
from .permissions import IsAuthorOrReadOnly


class CustomUserViewSet(viewsets.ModelViewSet):
    """Viewset for Custom User Object."""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Viewset for Post object."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)

