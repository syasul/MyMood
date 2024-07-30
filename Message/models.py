from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.message
    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email

