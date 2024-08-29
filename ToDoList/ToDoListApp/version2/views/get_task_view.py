from django.shortcuts import render
from django.views import View

from ToDoListApp.models import Task
from ToDoListApp.models.task import get_priority, get_state


class GetTaskView(View):
    def get(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        return render(
            request,
            "v2/v2_get_task_template.html",
            {
                "task": task,
                "priority": get_priority(task.priority),
                "state": get_state(task.state),
            },
        )
