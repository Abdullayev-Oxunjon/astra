from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from app.models import Features, Rooms, MainSocialNetwork, RoomImage, Blog, Service, Visitors, Subscribe


class CustomTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Features)
class FeaturesAdmin(CustomTranslationAdmin):
    list_display = ("title", "description")


@admin.register(Rooms)
class RoomsAdmin(CustomTranslationAdmin):
    list_display = ("title", "description")


@admin.register(Blog)
class BlogAdmin(CustomTranslationAdmin):
    list_display = ("title", "description", "short_description")


@admin.register(Service)
class ServiceAdmin(CustomTranslationAdmin):
    list_display = ("title", "description")


@admin.register(Visitors)
class VisitorsAdmin(CustomTranslationAdmin):
    list_display = ("visitor_title",)


admin.site.register([
    MainSocialNetwork,
    RoomImage,
    Subscribe
])
