from django.shortcuts import render
from django.http import HttpResponse
from events.forms import CategoryForm, EventForm,ParticipantForm
from events.models import Category, Event, Participant

# Create your views here.

def show_events(request):
    events = Event.objects.all()
    return render(request, "show_events.html",{'events': events})

def create_event(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Event created successfully!")
    return render(request, 'create_event.html', {'form': form})

def update_event(request,id):
    event = Event.objects.get(id=id)
    form = EventForm(instance=event)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponse("Event updated successfully!")
    return render(request, 'update_event.html', {'form': form})

def delete_event(request,id):
    if request.method == 'POST':
        event = Event.objects.get(id=id)
        event.delete()
    return HttpResponse("Event deleted successfully!")

def show_categories(request):
    categories = Category.objects.all()
    return render(request, "show_categories.html",{'categories': categories})

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

def delete_category(request,id):
    if request.method == 'POST':
        category = Category.objects.get(id=id)
        category.delete()
    return HttpResponse("Delete Category")

def show_participants(request):
    participants = Participant.objects.all()
    return render(request, "show_participants.html",{'participants': participants})

def create_participant(request):
    form = ParticipantForm()
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Participant created successfully!")
    return render(request, 'create_participant.html', {'form': form})