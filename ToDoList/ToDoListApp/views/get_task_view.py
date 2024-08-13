from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.models import Task2
from ToDoListApp.models.task2 import get_priority


@login_required
def get_task(request, task_id):
    task = Task2.objects.get(pk=task_id)
    return render(request, "get_task_template.html",
                  {'task': task, 'priority': get_priority(task.priority)})
