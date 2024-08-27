from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.models import Task
from ToDoListApp.models.task import get_priority, get_state


@login_required
def get_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(
        request,
        "v1/get_task_template.html",
        {"task": task, "priority": get_priority(task.priority),
         "state": get_state(task.state)},
    )
