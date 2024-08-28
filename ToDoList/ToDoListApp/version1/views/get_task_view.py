from django.shortcuts import render

from ToDoListApp.models import Task
from ToDoListApp.models.task import get_priority, get_state


def get_task_view(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(
        request,
        "v1/get_task_template.html",
        {"task": task, "priority": get_priority(task.priority),
         "state": get_state(task.state)},
    )
