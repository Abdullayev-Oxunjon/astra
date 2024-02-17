from django.urls import path

from app.views.blog import blog_view, publication_view
from app.views.main import index_view, contact_view, about_view
from app.views.rooms import rooms_view, room_view
from app.views.services import services_view, service_view
from app.views.other import bad_request_view
urlpatterns = [
    path('', index_view, name='index'),
    path('about/', about_view, name='about'),
    path('services/', services_view, name='services'),
    path('service/<int:service_id>/', service_view, name='service'),
    path('blog/', blog_view, name='blog'),
    path('contact/', contact_view, name='contact'),
    path('publication/<int:blog_id>/', publication_view, name='publication'),
    path('rooms/', rooms_view, name='rooms'),
    path('room/<int:room_id>/', room_view, name='room'),
    path('404/', bad_request_view, name='404'),
]
