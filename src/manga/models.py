from django.db import models
from django.utils.translation import gettext_lazy as _

from src.account.models import User
from src.base.services import get_path_upload_image, validate_size_image


class Genre(models.Model):
    """Жанры"""
    name = models.CharField(_('Название'), max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Жанр')
        verbose_name_plural = _('Жанры')


class Type(models.Model):
    name = models.CharField(_('Название'), max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Тип манга')
        verbose_name_plural = _('Типы манга')


class Manga(models.Model):
    genre = models.ManyToManyField(Genre, verbose_name=_('Жанры'))
    type = models.ForeignKey(Type, verbose_name=_('Тип'), on_delete=models.CASCADE)
    title = models.CharField(_('Название манги'), max_length=155)
    year = models.PositiveSmallIntegerField(_('Год'))
    poster = models.ImageField(_('Постер'), upload_to='posters')
    synopsis = models.TextField(_('Синопсис'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Манга')
        verbose_name_plural = _('Манга')


class Images(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(
        _('Изображения'),
        upload_to=get_path_upload_image,
        validators=[validate_size_image],
    )

    class Meta:
        verbose_name = _('Изображения')
        verbose_name_plural = _('Изображение')


class Comments(models.Model):
    """Комментарии"""
    manga = models.ForeignKey(Manga, verbose_name=_('Манга'), on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, verbose_name=_('Пользователь'), on_delete=models.CASCADE)
    comment = models.TextField(_('Комментарий'))

    def __str__(self):
        return self.user.nickname

    class Meta:
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')
