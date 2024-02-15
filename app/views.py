from django.shortcuts import render

from app.forms import SubscribeForm
from app.models import MainSocialNetwork, Features, Rooms, Blog, Service, Visitors


def index_view(request):
    rooms = Rooms.objects.all()
    social_networks = MainSocialNetwork.objects.all()
    features = Features.objects.all()
    blogs = Blog.objects.all()
    services = Service.objects.all()

    return render(request, 'app/index.html',
                  {'social_networks': social_networks,
                   'features': features,
                   "rooms": rooms,
                   "blogs": blogs,
                   "services": services})


def about_view(request):
    social_networks = MainSocialNetwork.objects.all()
    services = Service.objects.all()
    visitors = Visitors.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'app/about.html',
                  {'social_networks': social_networks,
                   "services": services,
                   "visitors": visitors,
                   "blogs": blogs})


def services_view(request):
    social_networks = MainSocialNetwork.objects.all()
    services = Service.objects.all()
    return render(request, 'app/services.html',
                  {'social_networks': social_networks,
                   "services": services})


def service_view(request):
    social_networks = MainSocialNetwork.objects.all()
    return render(request, 'app/service.html',
                  {'social_networks': social_networks})


def blog_view(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app/blog.html')

    form = SubscribeForm()
    social_networks = MainSocialNetwork.objects.all()
    popular_blogs = Blog.objects.order_by('-created_at')[:2]
    latest_blogs = Blog.objects.order_by("-created_at")[:6]
    publications = Blog.objects.order_by("-created_at")[:3]
    return render(request, 'app/blog.html',
                  {'social_networks': social_networks,
                   "popular_blogs": popular_blogs,
                   "latest_blogs": latest_blogs,
                   "publications": publications,
                   "form": form})


def contact_view(request):
    social_networks = MainSocialNetwork.objects.all()
    return render(request, 'app/contact.html',
                  {'social_networks': social_networks})


def publication_view(request):
    social_networks = MainSocialNetwork.objects.all()
    return render(request, 'app/publication.html',
                  {'social_networks': social_networks})


def rooms_view(request):
    social_networks = MainSocialNetwork.objects.all()
    rooms = Rooms.objects.all()
    return render(request, 'app/rooms.html',
                  {'social_networks': social_networks,
                   "rooms": rooms})


def room_view(request):
    social_networks = MainSocialNetwork.objects.all()
    return render(request, 'app/room.html',
                  {'social_networks': social_networks})


from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation


# This code sets the language
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response
