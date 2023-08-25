from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Genre, Type, Manga, Images, Comments


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display
    search_fields = ('name',)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display
    search_fields = ('name',)


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 0


@admin.register(Comments)
class CommentsInline(admin.ModelAdmin):
    list_display = ('manga', 'get_username', 'get_nickname', 'get_avatar')
    list_display_links = ('manga',)
    readonly_fields = ('user', 'manga',)
    search_fields = ('manga__title', 'comment',)
    list_filter = ('manga__title',)

    def get_username(self, object):
        return object.user.username

    def get_nickname(self, object):
        return object.user.nickname

    def get_avatar(self, object):
        if object.user.avatar:
            return mark_safe(f"<img src='{object.user.avatar.url}' width='50'>")

    get_username.short_description = 'Имя'
    get_nickname.short_description = 'Никнейм'
    get_avatar.short_description = 'Аватарка'


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'year', 'get_html_poster',)
    list_display_links = ('title',)
    search_fields = ('title', 'synopsis',)
    list_filter = ('type', 'genre', 'year',)
    inlines = (ImagesInline,)

    def get_html_poster(self, object):
        if object.poster:
            return mark_safe(f"<img src='{object.poster.url}' width='50'>")

    get_html_poster.short_description = 'Постер'
