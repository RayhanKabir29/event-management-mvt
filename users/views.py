from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from users.forms import RegistrationForm

# Create your views here.
def sign_up(request):
    if request.method == 'GET':
        form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    return render (request, 'registration/register.html',{"form":form})