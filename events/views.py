from django.shortcuts import render,redirect
from django.contrib import messages
from events.forms import EventForm
from events.models import Event, Category
from django.db.models import Q,Count
from django.utils.dateparse import parse_date
from django.utils import timezone

def home(request):
    upcoming_events = (
        Event.objects.prefetch_related('participant')
        .select_related('category')
        .filter(date__gte=timezone.now())
        .order_by('date')
        .annotate(participant_num=Count("participant"))
    ).order_by('?')[:6]
    context = {
        "upcoming_events": upcoming_events,
    }
    return render(request, "home.html", context)
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
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    events = (
        Event.objects.prefetch_related('participant')
        .select_related('category')
        .annotate(participant_num=Count("participant"))
    )
    
    search = request.GET.get('search', '')

    if search:
        events = events.filter(
            Q(name__icontains=search) |
            Q(location__icontains=search)
        )

    if type != 'All':
        events = events.filter(category__name=type)

    if start_date and end_date:
        start_date = parse_date(start_date) 
        end_date = parse_date(end_date)
        if start_date and end_date:
            events = events.filter(date__range=[start_date, end_date])

    categories = Event.objects.values_list('category__name', flat=True).distinct()

    context = {
        "events": events,
        "categories": categories
    }
    return render(request, "events.html", context)

from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

def event_detail(request, id):
    event = (
        Event.objects
        .prefetch_related('participant')
        .select_related('category')
        .annotate(participant_num=Count("participant"))
        .get(id=id)
    )

    context = {
        'event': event
    }
    return render(request, 'event_detail.html', context)

