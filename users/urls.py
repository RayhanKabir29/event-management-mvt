from django.urls import path
from users.views import *

urlpatterns = [
    path('sign-up/',sign_up, name='sign_up'),
    path('sign-in/',sign_in, name='sign_in'),
    path('sign-out/',sign_out, name='sign_out')
]
