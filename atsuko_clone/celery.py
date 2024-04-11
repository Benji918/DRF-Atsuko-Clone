from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atsuko_clone.settings')

app = Celery('atsuko_clone') 
app.conf.enable_utc = False

app.conf.update(timezone = 'Africa/Lagos')

# Configure Celery using settings from Django settings.py.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery beat settings
app.conf.beat_schedule = {
    'send-mail-every-day-8am': {
        'task': 'users.tasks.send_registration_email',
        'schedule': crontab(hour=1, minute=32),
    }
}

# Load tasks from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')