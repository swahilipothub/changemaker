from django import forms
from .models import Application

from core.utils import DateInput

SECTORS = (
    ('Technology', 'Technology and Innovation'),
    ('Art', 'Creativity and Art'),
    ('Healthcare', 'Promotion of Health'),
    ('Sports', 'Sports'),
    ('Environment', 'Environment'),
    ('Community', 'Community'),
)

STATUS = (
    ('PENDING', 'Pending Approval'),
    ('APPROVED', 'Approved'),
    ('DENIED', 'Denied'),
    ('CANCELLED', 'Cancelled')
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

SUBCOUNTY = (
    ('Mvita', 'Mvita'),
    ('Kisauni', 'Kisauni'),
    ('Nyali', 'Nyali'),
    ('Changamwe', 'Changamwe'),
    ('Jomvu', 'Jomvu'),
    ('Likoni', 'Likoni')
)

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]


class ApplicationForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "First Name",                
                "class": "form-control"
            }
        ))

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Last Name",                
                "class": "form-control"
            }
        ))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))

    subcounty = forms.CharField(
        widget=forms.Select(
            choices=SUBCOUNTY,
            attrs={
                "placeholder" : "Location",                
                "class": "form-control"
            }
        ))
    
    gender = forms.CharField(
        widget=forms.Select(
            choices=GENDER,
            attrs={
                "placeholder" : "Gender",                
                "class": "form-control"
            }
        ))
    
    birth_date = forms.DateField(widget=DateInput(
        attrs={
            "placeholder" : "Date of Birth",                
            "class": "form-control"
        }
    ))

    mobile_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Mobile Number",                
                "class": "form-control"
            }
        ))
    
    id_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "ID Number",                
                "class": "form-control"
            }
        ))
    
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
                "class": "form-control",
                'style': 'height: 10em;'
            }
        ))
    
    project_sector = forms.CharField(
        widget=forms.Select(
            choices=SECTORS,
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
        fields = (
            'first_name', 'last_name', 'email', 
            'subcounty', 'birth_date', 'id_number', 
            'mobile_number', 'gender', 'project_name', 
            'project_description', 'project_sector', 'people_impacted', 'status')