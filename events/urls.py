
from django.urls import path
from events.views import show_events,show_categories,show_participants

urlpatterns = [
    path('', show_events, name='events'),                
    path('categories/', show_categories, name='category'),  
    path('participants/', show_participants, name='participant'), 
]