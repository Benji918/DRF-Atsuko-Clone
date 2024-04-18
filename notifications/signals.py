from django.db.models.signals import post_save
from core.models import Notification, Product
from django.conf import settings
from django.dispatch import receiver
from .tasks import send_product_notification


@receiver(post_save, sender=Product)
def send_product_created_notification(sender, instance, created, **kwargs):
    if created:
        # Schedule the notification task asynchronously using Celery
        send_product_notification.delay(instance.merchant, instance.product_name)


