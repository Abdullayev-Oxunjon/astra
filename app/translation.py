from modeltranslation.translator import TranslationOptions, register

from .models import Features, Rooms, Blog, Service, Visitors, RoomFeatures, RoomAmenity, Faq, RoomCategory, Reviews


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


@register(RoomFeatures)
class RoomFeaturesTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(RoomAmenity)
class RoomAmenityTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


@register(RoomCategory)
class RoomCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Reviews)
class ReviewsTranslationOptions(TranslationOptions):
    fields = ( 'degree', 'description')
