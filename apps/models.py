from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(null=True)


class Todo(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
