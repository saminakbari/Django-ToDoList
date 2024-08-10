from django.http import HttpResponse
from django.shortcuts import render, redirect

from my_app.models import Task, ToDoList


def delete_task(request, task_id: int, list_id):
    task = Task.objects.get(pk=task_id)
    to_do_list = ToDoList.objects.get(pk=list_id)
    to_do_list.tasks.remove(task)
    to_do_list.save()
    sorted_tasks = sorted(to_do_list.tasks.all(), key=lambda x: x.deadline)
    sorted_tasks = sorted(sorted_tasks, key=lambda x: x.priority)
    return render(request, "get_list_template.html",
                  {"tasks": sorted_tasks, "user": to_do_list.owner,
                   "message": "Task deleted successfully.", "to_do_list": to_do_list})
