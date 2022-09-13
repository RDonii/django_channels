from django.shortcuts import render
from .models import Channels

def index(request):
    channels = Channels.objects.all()
    return render(request, 'index.html', {'channels': channels})

def room(request, channel_key):
    channel = Channels.objects.get(key=channel_key)
    return render(request, 'stream.html', {'channel': channel})