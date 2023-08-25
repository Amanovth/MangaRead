from rest_framework.views import APIView
from rest_framework import viewsets, filters, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .pagination import MangaPagination
from .filters import MangaFilter


class MangaListView(generics.ListAPIView):
    serializer_class = MangaListSerializer
    queryset = Manga.objects.all()
    pagination_class = MangaPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = MangaFilter


class MangaDetailView(viewsets.ViewSet):

    def retrieve(self, request, pk):
        try:
            queryset = Manga.objects.prefetch_related('comments__user').get(id=pk)
        except ObjectDoesNotExist:
            return Response({'detail': f"Объект с id {pk} не существует."})
        serializer = MangaDetailSerializer(queryset, context={'request': request})
        return Response(serializer.data)


class CommentCreateView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data, context={'request': request})

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'response': True}, status=201)


class GenreListView(viewsets.ViewSet):

    def list(self, request):
        queryset = Genre.objects.all()
        serializer = GenreListSerializer(queryset, many=True)
        return Response(serializer.data)
