from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    objects = CustomUserManager()


    def __str__(self):
        return self.email