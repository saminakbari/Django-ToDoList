import os

from celery import Celery

from ToDoListApp.models import ToDoList

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ToDoList.settings')

app = Celery('ToDoList')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

