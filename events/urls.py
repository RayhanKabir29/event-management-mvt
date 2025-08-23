
from django.urls import path
from events.views import home

urlpatterns = [
    path('show_events/',home)
]