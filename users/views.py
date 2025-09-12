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
    return render (request, 'auth/register.html',{"form":form})

def sign_in(request):
    if request.method == "GET":
         form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm()
        
    return render (request, 'auth/signin.html',{"form":form})