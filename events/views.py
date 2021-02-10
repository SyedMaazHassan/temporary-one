from django.shortcuts import render

# Create your views here.
def upcoming_events_view(request):
    return render(request, 'event.html')