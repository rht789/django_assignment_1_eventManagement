from django.urls import path
from events.views import *

urlpatterns = [
    path('home/',home),
    path('create_event/', create_event, name='create_event')
]
