import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'catalog.settings')

app = Celery('catalog')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
