from django import forms

from .views import UserProfile, TechStack, Project


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        exclude = ['user']
        

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']