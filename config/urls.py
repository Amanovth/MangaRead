from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .yasg import doc_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include("debug_toolbar.urls")),
    path('auth/', include('src.account.urls')),
    path('manga/', include('src.manga.urls'))
]

urlpatterns += doc_urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
