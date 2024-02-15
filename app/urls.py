from django.urls import path

from app.views import index_view, about_view, services_view, service_view, blog_view, contact_view, publication_view, \
    rooms_view, room_view

urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('services/', services_view, name='services'),
    path('service/', service_view, name='service'),
    path('blog/', blog_view, name='blog'),
    path('contact/', contact_view, name='contact'),
    path('publication/', publication_view, name='publication'),
    path('rooms/', rooms_view, name='rooms'),
    path('room/', room_view, name='room'),
]
