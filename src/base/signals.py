from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from src.manga.models import Images


@receiver(pre_delete, signal=Images)
def delete_image(sender, instance, **kwargs):
    instance.file.delete(False)
