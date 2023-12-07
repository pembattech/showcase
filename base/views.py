from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import UserProfile

# Create your views here.
def home(request):
    user_profile_instances = UserProfile.objects.get(id=1)
    context = {
        "user_profile": user_profile_instances,
    }
    return render(request, 'index.html', context=context)


