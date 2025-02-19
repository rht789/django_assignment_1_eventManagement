from django.shortcuts import render,redirect
from django.contrib import messages
from events.forms import EventForm
from events.models import Event, Category
from django.db.models import Q,Count

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
    type = request.GET.get('type', 'All')

    events = (Event.objects.prefetch_related('participant').select_related('category').annotate(participant_num=Count("participant")))

    if type != 'All':
        events = events.filter(category__name=type)

    categories = Event.objects.values_list('category__name', flat=True).distinct()

    context = {
        "events": events,
        "categories": categories
    }
    return render(request, "events.html", context)
