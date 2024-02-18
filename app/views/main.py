from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _

from app.forms import BookingModelForm, ContactForm
from app.models.blog import Blog
from app.models.other import MainSocialNetwork, Features
from app.models.rooms import Rooms
from app.models.services import Service, Reviews, Visitors


def index_view(request):
    if request.method == 'POST':
        form = BookingModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = BookingModelForm()

    rooms = Rooms.objects.all()
    social_networks = MainSocialNetwork.objects.all()
    features = Features.objects.all()
    blogs = Blog.objects.all()
    services = Service.objects.all()
    reviews = Reviews.objects.all()
    return render(request, 'app/index.html',
                  {'social_networks': social_networks,
                   'features': features,
                   "rooms": rooms,
                   "blogs": blogs,
                   "services": services,
                   "reviews": reviews,
                   "form": form})


def about_view(request):
    if request.method == 'POST':
        form = BookingModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = BookingModelForm()
    social_networks = MainSocialNetwork.objects.all()
    services = Service.objects.all()
    visitors = Visitors.objects.all()
    blogs = Blog.objects.all()
    reviews = Reviews.objects.all()
    return render(request, 'app/about.html',
                  {'social_networks': social_networks,
                   "services": services,
                   "visitors": visitors,
                   "blogs": blogs,
                   "reviews": reviews,
                   "form": form})


def contact_view(request):
    if request.method == 'POST':
        form_type = request.POST.get("form_type")

        if form_type == 'formOne':
            form = ContactForm(request.POST)
        elif form_type == 'formTwo':
            form = BookingModelForm(request.POST)
        else:
            # Default to ContactForm if form_type is not specified or unrecognized
            form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

        else:
            message = _("Ma'lumotlarni kiritishda xatolik sodir bo'ldi.Iltimos qayta kiriting")
            messages.add_message(request, messages.ERROR, message)
            return redirect('contact')

    # Default to ContactForm if it's a GET request or form_type is not specified
    form = ContactForm()
    social_networks = MainSocialNetwork.objects.all()
    return render(request, 'app/contact.html',
                  {'social_networks': social_networks,
                   "form": form})
