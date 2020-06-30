from django import forms
from .models import Application

SECTORS = (
        ('ENTERTAINMENT', 'Entertainment'),
        ('HEALTHCARE', 'Healthcare'),
        ('SPORTS', 'Sports'),
        ('ENVIRONMENT', 'Environment'),
        ('ECONOMIC', 'Economic'),
)

class ApplicationForm(forms.ModelForm):
    project_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "What is the name of your project",                
                "class": "form-control"
            }
        ))

    project_description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Please Describe your project",                
                "class": "form-control"
            }
        ))
    
    project_sector = forms.CharField(
        widget=forms.Select(choices=SECTORS,
            attrs={
                "placeholder" : "Which area / sector does your project fall in?",                
                "class": "form-control"
            }
        ))
    
    people_impacted = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "How many people has the project impacted?",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Application
        fields = ('project_name', 'project_description', 'project_sector', 'people_impacted',)