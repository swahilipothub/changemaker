from django import forms
from users.models import Profile
from .models import SMS, ATSettings, SMSTemplate


class SMSForm(forms.ModelForm):
    changemaker = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple, queryset = None)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = SMS
        fields = ('changemaker', 'message')

    def __init__(self, *args, **kwargs):
        super(SMSForm, self).__init__(*args, **kwargs)
        self.fields['changemaker'].queryset = Profile.objects.filter()


class SMSTemplateForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = SMSTemplate
        fields = ('name', 'message')


class ATSettingsForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}))
    api_key = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}))
    sender = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = ATSettings
        fields = ('username', 'api_key', 'sender')