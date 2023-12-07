from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
    
