
from django.contrib import admin
from django.urls import path,include
from events.views import organizer_dashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", organizer_dashboard, name="home"),
    path('events/',include('events.urls')),
]
 