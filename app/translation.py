from modeltranslation.translator import TranslationOptions, register

from .models import Features, Rooms, Blog, Service, Visitors


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
