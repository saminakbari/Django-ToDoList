from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.models import Task, ToDoList


@login_required
def delete_task_view(request, task_id: int, list_id):
    task = Task.objects.get(pk=task_id)
    to_do_list = ToDoList.objects.get(pk=list_id)
    to_do_list.tasks.remove(task)
    to_do_list.save()

    sorted_tasks = to_do_list.tasks.all().order_by("deadline", "priority")
    messages.add_message(request, messages.INFO, "Task deleted successfully.")
    return render(
        request,
        "v1/get_list_template.html",
        {"tasks": sorted_tasks, "user": to_do_list.owner, "to_do_list": to_do_list},
    )
