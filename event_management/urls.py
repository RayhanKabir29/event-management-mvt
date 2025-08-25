
from django.contrib import admin
from django.urls import path,include
from events.views import show_events


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", show_events, name="home"),
    path('events/',include('events.urls')),
]
 