from django.shortcuts import render
from django.http import HttpResponse
from events.forms import CategoryForm

# Create your views here.

def show_events(request):
    return render(request, "show_events.html")

def show_categories(request):
    return render(request, "show_categories.html")

def show_participants(request):
    return render(request, "show_participants.html")
def crete_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Category Created Successfully")
    return render(request, 'category.html', {'form': form})