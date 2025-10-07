from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title   
class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    participant_events = models.ManyToManyField(Event, related_name='events', blank=True)

    def __str__(self):
        return self.name 
    
# Signals 

# def notify_event_creation(sender, instance, created, **kwargs):
#     # Placeholder for notification logic
#     print('sender',sender)
#     print('instance',instance)
#     print('created',created)
#     print('kwargs',kwargs)


    