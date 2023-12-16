from django import forms

from .views import UserProfile, TechStack, Project


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']
        profile_picture = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'input-style'}))
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input-style'}),
            'bio': forms.Textarea(attrs={'class': 'textarea-style'}),
            'github_url': forms.URLInput(attrs={'class': 'input-style'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'input-style'}),
            'instagram_url': forms.URLInput(attrs={'class': 'input-style'}),
            'resume_url': forms.URLInput(attrs={'class': 'input-style'}),
        }

        
class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        exclude = ['user']
        widgets = {
            'language': forms.TextInput(attrs={'class': 'input-style'}),
            'framework': forms.TextInput(attrs={'class': 'input-style'}),
            'database': forms.TextInput(attrs={'class': 'input-style'}),
        }
        

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']
        widgets = {
            'project_title': forms.TextInput(attrs={'class': 'input-style'}),
            'project_description': forms.Textarea(attrs={'class': 'textarea-style'}),
            'project_github_url': forms.URLInput(attrs={'class': 'input-style'}),
            'project_livedemo': forms.URLInput(attrs={'class': 'input-style'}),
            'project_img1': forms.ClearableFileInput(attrs={'class': 'input-style'}),
            'project_img2': forms.ClearableFileInput(attrs={'class': 'input-style'}),
            
        }