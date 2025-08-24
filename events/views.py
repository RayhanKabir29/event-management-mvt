from django.shortcuts import render,redirect
from django.http import HttpResponse
from events.forms import CategoryForm, EventForm,ParticipantForm
from events.models import Category, Event, Participant
from django.contrib import messages

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
            messages.success(request, 'Event created successfully!')
            return redirect('create_event')
    return render(request, 'create_event.html', {'form': form})

def update_event(request,id):
    event = Event.objects.get(id=id)
    form = EventForm(instance=event)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event update successfully!')
            return redirect('update_event')
    return render(request, 'update_event.html', {'form': form})

def delete_event(request,id):
    if request.method == 'POST':
        event = Event.objects.get(id=id)
        event.delete()
        messages.success(request, 'Event delete successfully!')
        return redirect('show_events')
    

def show_categories(request):
    categories = Category.objects.all()
    return render(request, "show_categories.html",{'categories': categories})

def crete_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully!')
            return redirect('create_category')
    return render(request, 'create_category.html', {'form': form})

def update_category(request,id):
    category = Category.objects.get(id=id)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category update successfully!')
            return redirect('update_category')
    return render(request, 'edit_category.html', {'form': form})

def delete_category(request,id):
    if request.method == 'POST':
        category = Category.objects.get(id=id)
        category.delete()
        messages.success(request, 'Category delete successfully!')
        return redirect('show_categories')

def show_participants(request):
    participants = Participant.objects.all()
    return render(request, "show_participants.html",{'participants': participants})

def create_participant(request):
    form = ParticipantForm()
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Participant created successfully!')
            return redirect('show_participants')
    return render(request, 'create_participant.html', {'form': form})

def update_participant(request,id):
    participant = Participant.objects.get(id=id)
    form = ParticipantForm(instance=participant)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Participant update successfully!')
            return redirect('update_participants')
    return render(request, 'update_participant.html', {'form': form})

def delete_participant(request,id):
    if request.method == 'POST':
        participant = Participant.objects.get(id=id)
        participant.delete()
        messages.success(request, 'Participant delete successfully!')
        return redirect('show_participants')