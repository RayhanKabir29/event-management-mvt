from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from users.forms import RegistrationForm
from django.contrib import messages

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
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
       
        if user is not None:
            login(request, user)
            messages.success(request, "Log in Successfully")
            return redirect('home')
           
        else:
            messages.error(request, "Invalid Username Or Password")
    return render (request, 'auth/signin.html' )