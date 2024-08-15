from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.forms import TaskForm
from ToDoListApp.models import Task2, ToDoList2
from ToDoListApp.models.task2 import get_priority


@login_required
def edit_task(request, task_id, list_id):
    task = Task2.objects.get(pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.deadline = form.cleaned_data['deadline']
            task.priority = form.cleaned_data['priority']
            try:
                file = request.FILES['attachment']
                task.attachment = file
            except:
                pass
            try:
                if form.data['attachment-clear'] == 'on':
                    task.attachment.delete()
            except:
                pass
            task.save()
            messages.add_message(request, messages.INFO, "Task edited successfully.")

        else:
            errors = form.errors.items()
            for error in errors:
                messages.add_message(request, messages.ERROR, error[1][0])

        to_do_list = ToDoList2.objects.get(pk=list_id)
        sorted_tasks = to_do_list.tasks.all().order_by('deadline', 'priority')
        return render(request, "get_list_template.html",
                      {"tasks": sorted_tasks, "to_do_list": to_do_list,
                       "user": to_do_list.owner})

    else:
        form = TaskForm(initial={'title': task.title, 'description': task.description,
                                 'deadline': task.deadline, 'priority': task.priority,
                                 'attachment': task.attachment})
        return render(request, "edit_task_template.html",
                      {"task": task, "form": form})
