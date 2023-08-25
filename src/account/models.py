from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken

from ..base.services import get_path_upload_avatar, validate_size_image


class User(AbstractUser):
    nickname = models.CharField(
        _('Nickname'),
        max_length=150,
        unique=True,
        error_messages={
            'unique': _('A user with that nickname already exists.')
        },
    )

    avatar = models.ImageField(
        _('Profile Photo'),
        upload_to=get_path_upload_avatar,
        default='default_profile_photo.png',
        validators=[validate_size_image]
    )

    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.nickname

    def token(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
