from celery import shared_task
from core.models import Notification, CustomUser


@shared_task
def send_product_notification(recipient_id, product_name):
    # Retrieve the recipient object using the recipient_id
    recipient = CustomUser.objects.get(id=recipient_id)

    # Create an in-app notification for the recipient
    Notification.objects.create(
        recipient=recipient,
        message=f"A new product '{product_name}' has been added."
    )
    print('Successfully notified!!!!!')