
from django.urls import path
from events.views import show_events    

urlpatterns = [
    path('',show_events, name='events'),
]