from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import RegisterView, LoginView
from rest_framework_simplejwt.views import token_refresh

# router = DefaultRouter()
# router.register(r'register', RegisterViewSet, basename='register')
# router.register(r'login', LoginViewSet, basename='login')
#
# urlpatterns = router.urls

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token_refresh/', token_refresh, name='token_refresh')
]