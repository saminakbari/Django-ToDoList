from django.contrib import messages
from django.shortcuts import render
from django.views import View

from ToDoListApp.models import Task, ToDoList


class DeleteTaskView(View):
    def get(self, request, task_id, list_id):
        task = Task.objects.get(pk=task_id)
        to_do_list = ToDoList.objects.get(pk=list_id)
        to_do_list.tasks.remove(task)
        to_do_list.save()
        sorted_tasks = to_do_list.tasks.all().order_by("deadline", "priority")
        messages.add_message(request, messages.INFO, "Task deleted successfully.")
        return render(
            request,
            "v2/v2_get_list_template.html",
            {"tasks": sorted_tasks, "user": to_do_list.owner, "to_do_list": to_do_list},
        )
