from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app.views import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path("set_language/<str:language>", set_language, name="set-language"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# commit
urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    ]