import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ToDoList.settings')

app = Celery('ToDoList')
# app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://localhost:6379/0'

app.conf.beat_schedule = {
    'check-task': {
        'task': 'ToDoListApp.tasks.check_task_deadlines',
        'schedule': 24 * 3600,
        # 'schedule': 10 --> for test
    },
}
app.conf.timezone = 'UTC'

app.autodiscover_tasks()
