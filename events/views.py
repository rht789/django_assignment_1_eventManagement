from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from events.forms import EventForm

# Create your views here.
def home(request):
    return render(request,"home.html")
def create_event(request):
    event_form = EventForm()
    if request.method == 'POST':
        event_form=EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            messages.success(request,"Event created Sucessfully")
            return redirect('create_event')
    context = {"event_form": event_form}
    return render(request, "create_event.html", context)

def dashboard(request):
    return render(request,"dashboard.html")

def view_events(request):
    return render(request,"events.html")