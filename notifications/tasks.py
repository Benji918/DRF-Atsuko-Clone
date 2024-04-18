from celery import shared_task
from core.models import Notification

@shared_task
def send_product_notification(merchant, product_name):

    # Create an in-app notification for the merchant
    Notification.objects.create(
        recipient=merchant,
        message=f"A new product '{product_name}' has been added.",

    )
