from django import forms
import re
from django.contrib.auth.models import User
from users.models import *

class TailwindFormMixin:
    """Mixin to add TailwindCSS classes to form fields automatically"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = (
                'block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg '
                'shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
            )
            visible.field.widget.attrs['placeholder'] = visible.field.label


class RegistrationForm(TailwindFormMixin, forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']


    def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("This email is already registered. Please use another one.")
            return email
    def clean_password(self):
        password = self.cleaned_data.get('password')
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if not re.match(pattern, password):
            raise forms.ValidationError(
                "Password must be at least 8 characters long, include one uppercase letter, "
                "one lowercase letter, one number, and one special character (@, $, !, %, *, ?, &)."
            )
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")
        return cleaned_data
