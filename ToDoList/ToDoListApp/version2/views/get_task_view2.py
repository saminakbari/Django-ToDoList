from django.shortcuts import render
from django.views import View

from ToDoListApp.models import Task


class GetTask(View):
    def get(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        return render(request, "v2_get_task_template.html",
                      {'task': task, 'priority': Task.PRIORITY_CHOICES[int(task.priority) - 1][1]})
