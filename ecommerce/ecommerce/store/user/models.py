from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(max_length=250, default='Anonymous')
    email = models.EmailField(max_length=254, unique=True)

# sign up user using email and name
    username = models.EmailField(unique=True, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=11, blank=True, null=True)
    gender = models.CharField(max_length=11, blank=True, null=True)

    session_token = models.CharField(max_length=35, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
