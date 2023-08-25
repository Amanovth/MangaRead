from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """Путь к аватарке, format: (media)/profile_photos/user_id/photo.jpg
    """
    return f'profile_photos/user_{instance.id}/{file}'


def validate_size_image(file_obj):
    """ Проверка размера файла
    """
    megabyte_limit = 3
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Maximum file size {megabyte_limit}MB")


def get_path_upload_image(instance, file):
    """Путь к изображению, format: (media)/images/manga_id/image.jpg
    """
    return f"images/{instance.manga.id}/{file}"
