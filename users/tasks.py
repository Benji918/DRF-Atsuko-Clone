import ssl
from celery import shared_task
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from django.conf import settings

@shared_task(bind=True)
def send_registration_email(
        sender_email=settings.SENDER_EMAIL,
        password=settings.SENDER_EMAIL_PASSWORD,
        receiver_email=None,
        message='Thank you for registering on our site.'
):
    
    # Create a MIME object
    msg = MIMEMultipart()
    
    # Attach the message
    msg.attach(MIMEText(message, "plain"))
    
    # Set the email subject, sender, and receiver
    msg["Subject"] = 'Welcome to Our Site!'
    msg["From"] = sender_email
    msg["To"] = receiver_email


    # Establish a connection to the SMTP server
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        # Log in to the email account
        server.login(sender_email, password)
        
        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())