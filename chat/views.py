# chat/views.py
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Room
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, "chat/index.html")

@login_required(login_url='/accounts/login/')
def room(request, room_name):
    user_id = request.user.id
    return render(request, "chat/room.html", {"room_name": room_name, "user_id": user_id})

@login_required(login_url='/accounts/login/')
def room_list(request):
    chat_rooms = Room.objects.all()

    context = {'chat_rooms': chat_rooms}
    return render(request, 'chat/room_list.html', context)

@require_http_methods(["POST"])
def create_room(request):
    room_name = request.POST.get('room_name')
    if room_name:
        Room.objects.get_or_create(name=room_name)
    return redirect('chat:room_list')
@require_http_methods(["POST"])
def delete_room(request, room_name):
    try:
        room = Room.objects.get(name=room_name)
        room.delete()
        return HttpResponseRedirect(reverse('chat:room_list'))
    except Room.DoesNotExist:
        logger.warning(f"Room with name '{room_name}' does not exist.")
        return HttpResponseRedirect(reverse('chat:room_list'))
    except Exception as e:
        logger.error(f"Error deleting room '{room_name}': {e}")
        return JsonResponse({'error': 'Could not delete room'}, status=500)
