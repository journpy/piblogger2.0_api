from django.db import models
from users.models import CustomUser


class Post(models.Model):
    """Model a Post object."""
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255)


    def __str__(self):
        """Return a string representation of Post object."""
        return self.title