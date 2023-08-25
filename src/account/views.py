from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from .serializers import *


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterViewSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': _('User registered successfully.')}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
