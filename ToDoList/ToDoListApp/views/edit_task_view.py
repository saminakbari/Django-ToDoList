from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.models import Task2, ToDoList2


@login_required
def edit_task(request, task_id, list_id):
    task = Task2.objects.get(pk=task_id)
    if request.method == 'GET':
        return render(request, "edit_task_template.html",
                      {"task": task})

    else:
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.deadline = request.POST.get('deadline')
        task.priority = request.POST.get('priority')
        task.save()
        to_do_list = ToDoList2.objects.get(pk=list_id)
        sorted_tasks = to_do_list.tasks.all().order_by('deadline', 'priority')
        messages.add_message(request, messages.INFO, "Task edited successfully.")
        return render(request, "get_list_template.html",
                      {"tasks": sorted_tasks, "to_do_list": to_do_list,
                       "user": to_do_list.owner})
