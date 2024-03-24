from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import smtplib, ssl
from celery import shared_task
from django.conf import settings

@shared_task(bind=True)
def send_registration_email(self, receiver_email, message='Thank you for registering on our site.'):
    # Create a MIME object
    msg = MIMEMultipart()
        
    # Attach the message
    msg.attach(MIMEText(message, "plain"))

    # Set the email subject, sender, and receiver
    msg["Subject"] = 'welcome to GFG world'
    msg["From"] = settings.EMAIL_HOST_USER
    msg["To"] = receiver_email

    # Establish a connection to the SMTP server
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        # Log in to the email account
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        
        # Send the email
        server.sendmail(settings.EMAIL_HOST_USER, receiver_email, msg.as_string())
    return 'Email Sent Successfully!!!'