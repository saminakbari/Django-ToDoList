import django

from ToDoListApp.celery import app
from ToDoListApp.models import Task


@app.task()
def check_task_deadlines():
    for task in Task.objects.all():
        if task.deadline <= django.utils.timezone.now().date():
            task.state = True
            task.save()
            print("I'm working.")
    return "finished"
