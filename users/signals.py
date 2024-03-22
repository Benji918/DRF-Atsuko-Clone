from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .tasks import send_registration_email

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_email_registration_on_register(sender, instance, created, **kwargs):
    if created:
        email = instance.email
        send_registration_email.delay(receiver_email=email)