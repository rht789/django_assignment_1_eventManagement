from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from events.forms import EventForm

# Create your views here.
def home(request):
    return render(request,"dashboard.html")
def create_event(request):
    event_form = EventForm()
    if request.method == 'POST':
        event_form(request.POST)
        if event_form.isvalid():
            event_form.save()
        messages.success(request,"Event created Sucessfully")
        redirect('create_')