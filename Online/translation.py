from .models import UserProfile
from modeltranslation.translator import TranslationOptions, register


@register(UserProfile)
class HotelTranslationOptions(TranslationOptions):
    fields = ('user', 'nickname')
