from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.models import Task2, ToDoList2


@login_required
def delete_task(request, task_id: int, list_id):
    task = Task2.objects.get(pk=task_id)
    to_do_list = ToDoList2.objects.get(pk=list_id)
    to_do_list.tasks.remove(task)
    to_do_list.save()

    sorted_tasks = to_do_list.tasks.all().order_by('deadline', 'priority')
    messages.add_message(request, messages.INFO, "Task deleted successfully.")
    return render(request, "get_list_template.html",
                  {"tasks": sorted_tasks, "user": to_do_list.owner,
                   "to_do_list": to_do_list})
