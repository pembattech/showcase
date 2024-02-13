from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile, TechStack, Project
from .forms import *



def custom_404(request, exception):
    return render(request, '404.html', status=404)

def home(request):
    # try: 
    user_profile_instances = UserProfile.objects.all().first()
    user_profile_instance = user_profile_instances

    # Check if user_profile_instance is not None before proceeding
    if user_profile_instance:
        tech_stacks = TechStack.objects.filter(user=user_profile_instance).first()
        project_instances = Project.objects.filter(user=user_profile_instance)

        context = {
            "user_profile": user_profile_instance,
            "tech_stack": tech_stacks,
            "projects": project_instances
        }
        return render(request, 'index.html', context=context)
    else:
        return render(request, '404.html')

def update_showcase(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return render(request, '404.html')

    username = request.user.username
    user_profile = get_object_or_404(UserProfile, user__username=username)
    projects = Project.objects.filter(user=user_profile)
    techstack = TechStack.objects.filter(user=user_profile).first()

    # Initialize forms
    userprofile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=user_profile)

    if not techstack:
        techstack = TechStack(user=user_profile)

    techstack_form = TechStackForm(request.POST or None, instance=techstack)
    project_forms = [ProjectForm(request.POST or None, request.FILES or None, prefix=str(project.id), instance=project) for project in projects]

    # Check if the request method is POST
    if request.method == "POST":
        # Validate forms
        if (
            userprofile_form.is_valid()
            and techstack_form.is_valid()
            and all(project_form.is_valid() for project_form in project_forms)
        ):
            # Update user profile
            user_profile = userprofile_form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            # Update tech stack
            techstack_form.save(commit=False)
            techstack_form.user = request.user
            techstack_form.save()

            # Update existing projects
            for project_form in project_forms:
                project_form.save(commit=False)
                project_form.user = request.user
                project_form.save()

            return redirect('home')

    # Render the update_showcase template with the forms
    return render(request, 'update_showcase.html', {
        'userprofile_form': userprofile_form,
        'techstack_form': techstack_form,
        'project_forms': project_forms,
    })

def add_project(request):
    if not request.user.is_authenticated:
        return render(request, '404.html')

    # Initialize forms
    new_project_form = ProjectForm(request.POST or None, request.FILES or None)

    # Check if the request method is POST
    if request.method == "POST":
        new_project_form = ProjectForm(request.POST, request.FILES)
        if new_project_form.is_valid():
            # Save the new project
            new_project = new_project_form.save(commit=False)
            new_project.user = request.user.userprofile
            new_project.save()

        return redirect('home')

    return render(request, 'add_project.html', {
        'new_project': new_project_form,
    })

def delete_project(request, project_id):
    if request.user.is_authenticated:
        project = get_object_or_404(Project, id=project_id, user=request.user.userprofile)
        project.delete()
        return redirect('update_showcase')
    else:
        return render(request, '404.html')
    
def logout_user(request):
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        return redirect("home")
    else:
        return render(request, '404.html')

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
    
def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        user_profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()
            return redirect('home')
    else:
        user_form = UserCreationForm()
        user_profile_form = UserProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'user_profile_form': user_profile_form})