from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
from modeltranslation.admin import TranslationAdmin
from .models import UserProfile

admin.site.register(UserProfile)

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
admin.site.register(Category)
admin.site.register(ProductPhotos)
admin.site.register(Comment)
