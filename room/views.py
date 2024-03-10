from django.shortcuts import render

# Create your views here.
from .models import Room, Message
from django.contrib.auth.decorators import login_required

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    return render(request, 'room/room.html', {'room': room, 'messages':messages})