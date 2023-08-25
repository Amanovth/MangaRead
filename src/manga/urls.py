from django.urls import path
from .views import MangaListView, MangaDetailView, CommentCreateView, GenreListView

urlpatterns = [
    path('list/', MangaListView.as_view(), name='manga-list'),
    path('detail/<int:pk>/', MangaDetailView.as_view({'get': 'retrieve'}), name='manga-detail'),
    path('create-comment/', CommentCreateView.as_view({'post': 'create'}), name='create-comment'),
    path('genre-list/', GenreListView.as_view({'get': 'list'}), name='genre-list')
]
