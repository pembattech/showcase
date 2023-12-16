from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='showcase/profile_pic', blank=True, null=True)
    email = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    github_url = models.URLField(max_length=255, null=True, blank= False)
    linkedin_url = models.URLField(max_length=255, null=True, blank= False)
    instagram_url = models.URLField(max_length=255, null=True, blank= False)
    resume_url = models.URLField(max_length=255, null=True, blank= False)

    def __str__(self):
        return self.user.username

# Signal handlers
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    
class TechStack(models.Model):
    language = models.CharField(max_length=255, null=True, blank=False)
    framework = models.CharField(max_length=255, null=True, blank=False)
    database = models.CharField(max_length=255, null=True, blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.language

class Project(models.Model):
    project_title = models.CharField(max_length=255)
    project_description = models.CharField(max_length=255)
    project_livedemo = models.CharField(max_length=255)
    project_github_url = models.URLField(max_length=255, null=True, blank= False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    project_img1 = models.ImageField(upload_to='showcase/projectimg', null=True, blank=False)
    project_img2 = models.ImageField(upload_to='showcase/projectimg', null=True, blank=False)
    
    def __str__(self) -> str:
        return self.project_title