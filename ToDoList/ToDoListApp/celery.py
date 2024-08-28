import os

from celery import Celery
from celery.schedules import crontab

from ToDoList import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ToDoList.settings')

app = Celery('ToDoList')
# app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = settings.REDIS_HOST

app.conf.timezone = 'UTC'
app.conf.beat_schedule = {
    'check-task': {
        'task': 'ToDoListApp.tasks.check_task_deadlines',
        'schedule': crontab(hour='0', minute='0')
        # 'schedule': 24 * 3600,
        # 'schedule': 10
    },
}

app.autodiscover_tasks()
