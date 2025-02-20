from django.urls import path
from events.views import *

urlpatterns = [
    path('home/',home, name='home'),
    path('create_event/', create_event, name='create_event'),
    path('dashboard/', dashboard, name='dashboard'),
    path('events/', view_events, name='events'),
    path('events/<int:id>', event_detail, name='event_detail'),
]
