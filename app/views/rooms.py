from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from app.forms import BookingModelForm
from app.models.other import MainSocialNetwork
from app.models.rooms import Rooms, RoomCategory


def rooms_view(request):
    if request.method == 'POST':
        form = BookingModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = BookingModelForm()
    social_networks = MainSocialNetwork.objects.all()
    rooms = Rooms.objects.all().order_by('-id')
    paginator = Paginator(rooms, per_page=6)
    page_number = request.GET.get('page', 1)
    rooms_list = paginator.get_page(page_number)
    search_results = rooms.count()
    categories = RoomCategory.objects.all()
    return render(request, 'app/rooms.html',
                  {'social_networks': social_networks,
                   "rooms": rooms_list,
                   "search_results": search_results,
                   "categories": categories,
                   "form": form})


def room_view(request, room_id):
    social_networks = MainSocialNetwork.objects.all()
    room = Rooms.objects.filter(id=room_id).first()
    rooms = Rooms.objects.all()
    if request.method == "POST":
        form = BookingModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookingModelForm()

    return render(request, 'app/room.html',
                  {'social_networks': social_networks,
                   "room": room,
                   "rooms": rooms,
                   "form": form})
