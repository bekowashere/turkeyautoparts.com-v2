from django.contrib import admin
from parler.admin import TranslatableAdmin
from glossary.models import GlossaryCategory, GlossaryTerm
from django.utils.translation import gettext_lazy as _

@admin.register(GlossaryTerm)
class GlossaryTermAdmin(TranslatableAdmin):
    fieldsets = (
        (_('Term Information'), {'fields': ('short_name', 'long_name', 'slug', 'category')}),
        (_('Image Information'), {'fields': ('image', 'image_url', 'image_path')}),
        (_('Description'), {'fields': ('description',)}),
        (_('Source Website'), {'fields': ('detail_url', 'source_site',)})
    )

    list_display = ('long_name', 'short_name', 'slug', 'category')
    list_filter = ('category', 'source_site')
    search_fields = ('long_name', 'slug', 'category__name')
    ordering = ('long_name',)

@admin.register(GlossaryCategory)
class GlossaryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    search_fields= ('name', 'slug')
    ordering = ('name',)

