from django.contrib import admin
from .models import UserProfile, TechStack, Project

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(TechStack)
admin.site.register(Project)