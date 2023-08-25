import django_filters
from .models import Manga


class CharFilterInFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass


class MangaFilter(django_filters.FilterSet):
    genre = CharFilterInFilter(field_name='genre__name', lookup_expr='in')
    title = django_filters.CharFilter(field_name='title', lookup_expr='in')

    class Meta:
        model = Manga
        fields = ['genre']
