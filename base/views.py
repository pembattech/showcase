from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile, TechStack, Project
from .forms import *



def custom_404(request, exception):
    return render(request, '404.html', status=404)

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
        return render(request, '404.html')
    
    
def update_showcase(request):
    if request.user.is_authenticated:
        username = request.user.username
        
        user_profile = get_object_or_404(UserProfile, user__username = username)
        techstack = get_object_or_404(TechStack, user=user_profile)
        project = get_object_or_404(Project, user = user_profile)

        userprofile_form = UserProfileForm(instance=user_profile)
        techstack_form = TechStackForm(instance=techstack)
        project_form = ProjectForm(instance=project)

        if request.method == "POST":
            userprofile_form = UserProfileForm(request.POST, instance=user_profile)
            techstack_form = TechStackForm(request.POST, instance=techstack)
            project_form = ProjectForm(request.POST, instance=project)
            
            if userprofile_form.is_valid() and techstack_form.is_valid() and project_form.is_valid():

                userprofile_form.save()
                techstack_form.save()
                project_form.save()
                
                return redirect('home')
                
        return render(request, 'update_showcase.html', {'userprofile_form': userprofile_form, 'techstack_form': techstack_form, 'project_form': project_form})
    else:
        return redirect('home')

def logout_user(request):
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        print(f"Logout successful. User '{username}' has been logged out.")
        return redirect("login")
    else:
        return HttpResponse("No user is currently logged in.")

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            form.save()

            return redirect("login")

    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})

def login_user(request):
    if request.method == "POST":
        try:
            fetch_username = request.POST["username"]
            fetch_password = request.POST["password"]

            print(fetch_username, fetch_password)

            user = authenticate(
                request, username=fetch_username, password=fetch_password
            )
            if user is not None:
                login(request, user)

                return redirect("home")
            else:
                return HttpResponse("Invalid credentials.")
        except Exception as e:
            return HttpResponse("Error occur in login.")
    else:
        return render(request, "login.html")