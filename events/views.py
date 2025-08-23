from django.shortcuts import render
from django.http import HttpResponse
from events.forms import CategoryForm
from events.models import Category

# Create your views here.

def show_events(request):
    return render(request, "show_events.html")


def show_categories(request):
    categories = Category.objects.all()
    return render(request, "show_categories.html",{'categories': categories})

def show_participants(request):
    return render(request, "show_participants.html")

def crete_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Category Created Successfully")
    return render(request, 'create_category.html', {'form': form})

def update_category(request,id):
    category = Category.objects.get(id=id)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponse("Category Update Successfully")
    return render(request, 'edit_category.html', {'form': form})