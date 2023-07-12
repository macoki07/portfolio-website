from django import forms
from django.forms import ModelForm
from portfolio.models import Profile, Project, Section
from django.core.validators import FileExtensionValidator

class EditProfileForm(ModelForm):
    picture = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )

    class Meta:
        model = Profile
        fields = ("name", "mission", "about", "picture")
        labels = {
            "name": "Name:",
            "mission": "Mission:",
            "about": "About:",
            "picture": "Picture:",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "mission": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Mission"}
            ),
            "about": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "About"}
            ),
        }

class EditSectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ("title", "description", "priority")
        labels = {
            "title": "Title:",
            "description": "Content:",
            "priority": "Priority:",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Details (in markdown)\nPlease hit 'Enter' every 2 lines of text", "style": " resize: none;",}
            ),
            "priority": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Priority"}
            ),
        }

class AddSectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ("title", "description")
        labels = {
            "title": "Title:",
            "description": "Content:",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Details (in markdown)\nPlease hit 'Enter' every 2 lines of text", "style": " resize: none;",}
            ),
        }

class EditProjectForm(ModelForm):
    media = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )

    class Meta:
        model = Project
        fields = ("title", "short_description", "details", "priority", "media")
        labels = {
            "title": "Title:",
            "short_description": "Description:",
            "details": "Details:",
            "priority": "Priority:",
            "media": "Media:", 
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title"}
            ),
            "short_description": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Description"}
            ),
            "details": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Details (in markdown)"}
            ),
            "priority": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Priority"}
            ),
        }

class AddProjectForm(ModelForm):
    media = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    
    class Meta:
        model = Project
        fields = ("title", "short_description", "details", "media")
        labels = {
            "title": "Title:",
            "short_description": "Description:",
            "details": "Details:",
            "media": "Media:", 
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Title"}
            ),
            "short_description": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Description"}
            ),
            "details": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Details (in markdown)"}
            ),
        }