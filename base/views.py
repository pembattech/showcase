from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile, TechStack, Project
from .forms import *



def custom_404(request, exception):
    return render(request, '404.html', status=404)

def home(request):
    user_profile_instances = UserProfile.objects.get(id=1)
    user_profile_instance = user_profile_instances

    # Check if user_profile_instance is not None before proceeding
    if user_profile_instance:
        tech_stacks = TechStack.objects.filter(user=user_profile_instance).first()
        project_instances = Project.objects.filter(user=user_profile_instance)

        print(project_instances)
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
        
        user_profile = get_object_or_404(UserProfile, user__username=username)
        techstack = get_object_or_404(TechStack, user=user_profile)
        projects = Project.objects.filter(user=user_profile)

        userprofile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=user_profile)
        techstack_form = TechStackForm(request.POST or None, instance=techstack)
        project_forms = [ProjectForm(request.POST or None, prefix=str(project.id), instance=project) for project in projects]
        new_project_form = ProjectForm()

        if request.method == "POST":
            
            if (
                userprofile_form.is_valid()
                and techstack_form.is_valid()
                and all(project_form.is_valid() for project_form in project_forms)
                ):
                user_profile = userprofile_form.save(commit=False)
                user_profile.user = request.user  # Set the user manually since it's not part of the form
                user_profile.save()
                
                techstack_form.save()

                for project_form in project_forms:
                    project_form.save()
                    
                new_project_form = ProjectForm(request.POST)
                if new_project_form.is_valid():
                    new_project = new_project_form.save(commit=False)
                    new_project.user = request.user.userprofile
                    new_project.save()
                    

                return redirect('home')
                
        return render(request, 'update_showcase.html', {
            'userprofile_form': userprofile_form,
            'techstack_form': techstack_form,
            'project_forms': project_forms,
            'new_project': new_project_form,
        })
    else:
        return render(request, '404.html')
    
def logout_user(request):
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        return redirect("home")
    else:
        return render(request, '404.html')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
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