from django.shortcuts import render
from .models import UserProfile, TechStack, Project

def home(request):
    user_profile_instances = UserProfile.objects.filter(id=1)
    
    # Usingfirst() to get the first instance
    user_profile_instance = user_profile_instances.first()

    # Check if user_profile_instance is not None before proceeding
    if user_profile_instance:
        tech_stacks = TechStack.objects.filter(user=user_profile_instance).first()
        project_instances = Project.objects.filter(user=user_profile_instance).first()
        context = {
            "user_profile": user_profile_instance,
            "tech_stack": tech_stacks,
            "projects": project_instances
        }
        return render(request, 'index.html', context=context)
    else:
        return render(request, 'error.html')
