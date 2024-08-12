from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.models import Task


@login_required
def get_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, "get_task_template.html",
                  {'task': task, 'priority': Task.PRIORITY_CHOICES[int(task.priority) - 1][1]})
