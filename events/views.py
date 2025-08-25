from django.shortcuts import render,redirect
from django.http import HttpResponse
from events.forms import CategoryForm, EventForm,ParticipantForm
from events.models import Category, Event, Participant
from django.contrib import messages
from django.db.models import Count, Sum,Q
from django.utils.dateparse import parse_date
from django.utils.timezone import now

# Create your views here.
def show_events(request):
    events = (
        Event.objects
        .select_related("category")
        .prefetch_related("events")  
        .annotate(total_participants=Count("events"))
    )
    category_id = request.GET.get("category")  
    start_date = request.GET.get("start_date") 
    end_date = request.GET.get("end_date") 
    search = request.GET.get("search")    

    if category_id:
        events = events.filter(category_id=category_id)

    if start_date and end_date:
        events = events.filter(
            date__range=[parse_date(start_date), parse_date(end_date)]
        )
    if search:
        events = events.filter(
            Q(title__icontains=search) | Q(location__icontains=search)
        )
    total_participants_across_all = events.aggregate(
        total=Sum("total_participants")
    )["total"] or 0
    categories = Category.objects.all()

    return render(
        request,
        "show_events.html",
        {
            "events": events,
            "total_participants_across_all": total_participants_across_all,
            "categories": categories,
        },
    )

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
            return redirect('events')
    return render(request, 'update_event.html', {'form': form})

def delete_event(request,id):
    if request.method == 'POST':
        event = Event.objects.get(id=id)
        event.delete()
        messages.success(request, 'Event delete successfully!')
        return redirect('events')
    

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
            return redirect('category')
    return render(request, 'edit_category.html', {'form': form})

def delete_category(request,id):
    if request.method == 'POST':
        category = Category.objects.get(id=id)
        category.delete()
        messages.success(request, 'Category delete successfully!')
        return redirect('category')

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
            return redirect('create_participant')
    return render(request, 'create_participant.html', {'form': form})

def update_participant(request,id):
    participant = Participant.objects.get(id=id)
    form = ParticipantForm(instance=participant)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Participant update successfully!')
            return redirect('participant')
    return render(request, 'update_participant.html', {'form': form})

def delete_participant(request,id):
    if request.method == 'POST':
        participant = Participant.objects.get(id=id)
        participant.delete()
        messages.success(request, 'Participant delete successfully!')
        return redirect('participant')
    
def organizer_dashboard(request):
    today = now().date()

    # --- Stats ---
    total_participants = Participant.objects.count()
    total_events = Event.objects.count()
    upcoming_events = Event.objects.filter(date__gte=today).count()
    past_events = Event.objects.filter(date__lt=today).count()

    # --- Today’s Events ---
    todays_events = Event.objects.filter(date=today)

    # --- Interactive Filter (by query param) ---
    filter_type = request.GET.get("filter")  # 'all', 'upcoming', 'past'

    if filter_type == "upcoming":
        events = Event.objects.filter(date__gte=today)
    elif filter_type == "past":
        events = Event.objects.filter(date__lt=today)
    else:
        events = Event.objects.all()  # default: show all

    return render(
        request,
        "organized_dashboard/organizer_dashboard.html",
        {
            "total_participants": total_participants,
            "total_events": total_events,
            "upcoming_events": upcoming_events,
            "past_events": past_events,
            "todays_events": todays_events,
            "events": events,
            "filter_type": filter_type or "all",
        },
    )