from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from app.models.blog import Blog, BlogComment
from app.models.other import Features, MainSocialNetwork, Contact
from app.models.rooms import Rooms, RoomFeatures, RoomAmenity, RoomCategory, RoomImage, Booking
from app.models.services import Service, Visitors, Faq, Reviews, Subscribe


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
    list_display = ("title", "description", "short_description", "created_at", "updated_at")


@admin.register(Service)
class ServiceAdmin(CustomTranslationAdmin):
    list_display = ("title", "description")


@admin.register(Visitors)
class VisitorsAdmin(CustomTranslationAdmin):
    list_display = ("visitor_title",)


@admin.register(RoomFeatures)
class RoomFeaturesAdmin(CustomTranslationAdmin):
    list_display = ("title",)


@admin.register(RoomAmenity)
class RoomAmenityAdmin(CustomTranslationAdmin):
    list_display = ("title", "description")


@admin.register(Faq)
class FaqAdmin(CustomTranslationAdmin):
    list_display = ("question", "answer")


@admin.register(RoomCategory)
class RoomCategoryAdmin(CustomTranslationAdmin):
    list_display = ("title",)


@admin.register(Reviews)
class ReviewsAdmin(CustomTranslationAdmin):
    list_display = ("degree", "description")


admin.site.register([
    MainSocialNetwork,
    RoomImage,
    Subscribe,
    Contact,
    Booking,
    BlogComment
])
