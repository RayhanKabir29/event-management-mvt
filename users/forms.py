from django import forms
from django.contrib.auth.models import User
from users.models import *

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','password','confirm_password']
    
    def clean_password(self):
            password = self.cleaned_data.get('password')
            
            if len(password)<8:
                raise forms.ValidationError("Password Must  Be 8 Charachter Long")