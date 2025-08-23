
from django.urls import path
from events.views import show_events,show_categories,show_participants,crete_category,update_category

urlpatterns = [
    path('', show_events, name='events'),    
    path('categories/create/', crete_category, name='create_category'),  
     path('categories/update/<int:id>', update_category, name='update_category'),           
    path('categories/', show_categories, name='category'),  
    path('participants/', show_participants, name='participant'), 
]