from django.shortcuts import redirect, render

from app.forms import BookingModelForm
from app.models import MainSocialNetwork, Service, Rooms, Faq


def services_view(request):
    if request.method == 'POST':
        form = BookingModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = BookingModelForm()
    social_networks = MainSocialNetwork.objects.all()
    services = Service.objects.all()
    return render(request, 'app/services.html',
                  {'social_networks': social_networks,
                   "services": services,
                   "form": form})


def service_view(request, service_id):
    if request.method == 'POST':
        form = BookingModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = BookingModelForm()
    social_networks = MainSocialNetwork.objects.all()
    service = Service.objects.filter(id=service_id).first()
    services = Service.objects.all()[:3]
    rooms = Rooms.objects.all()
    faqs = Faq.objects.all()
    return render(request, 'app/service.html',
                  {'social_networks': social_networks,
                   "service": service,
                   "services": services,
                   "rooms": rooms,
                   "faqs": faqs,
                   "form": form})
