from django import forms
from users.models import Profile
from .models import SMS


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