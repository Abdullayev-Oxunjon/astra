from modeltranslation.translator import TranslationOptions, register

from app.models.blog import Blog
from app.models.other import Features
from app.models.rooms import Rooms,  RoomAmenity, RoomCategory
from app.models.services import Service, Visitors, Faq, Reviews


@register(Features)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Rooms)
class RoomsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'short_description')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Visitors)
class VisitorsTranslationOptions(TranslationOptions):
    fields = ('visitor_title',)







@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


@register(RoomCategory)
class RoomCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Reviews)
class ReviewsTranslationOptions(TranslationOptions):
    fields = ( 'degree', 'description')
