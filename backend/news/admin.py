from django.contrib import admin
from parler.admin import TranslatableAdmin
from news.models import Category, Tag, NewsItem
from django.utils.translation import gettext_lazy as _


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Category Information'), {'fields': ('name', 'slug')}),
    )
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Tag Information'), {'fields': ('name', 'slug')}),
    )
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('name',)


@admin.register(NewsItem)
class NewsItemAdmin(TranslatableAdmin):
    fieldsets = (
        (_('News Information'), {'fields': ('id', 'user', 'title', 'slug', 'image')}),
        (_('Depends'), {'fields': ('category', 'tags')}),
        (_('Content'), {'fields': ('content',)}),
        (_('Status'), {'fields': ('status',)}),
        (_('Metadata'), {'fields': ('created_date', 'updated_date')}),
    )
    list_display = ('title', 'slug', 'user')
    search_fields = ('title', 'slug', 'user__username', 'user__email')
    ordering = ('created_date',)
    readonly_fields = ('id','created_date', 'updated_date')