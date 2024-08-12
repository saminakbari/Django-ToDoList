from django.http import HttpResponse
from django.shortcuts import render, redirect

from my_app.forms.create_task_form import CreateTaskForm
from my_app.models import Task, ToDoList


def create_task(request, list_id):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            deadline = form.cleaned_data['deadline']
            priority = form.cleaned_data['priority']
            task = Task(title=title, description=description, deadline=deadline, priority=priority)
            task.save()
            to_do_list = ToDoList.objects.get(pk=list_id)
            task.to_do_lists.add(to_do_list)
            task.owner = to_do_list.owner
            task.save()

            sorted_tasks = sorted(to_do_list.tasks.all(), key=lambda x: x.deadline)
            sorted_tasks = sorted(sorted_tasks, key=lambda x: x.priority)
            return render(request, "get_list_template.html",
                          {"tasks": sorted_tasks, "to_do_list": to_do_list, "user": to_do_list.owner,
                           "message": "Task created successfully."})

    else:
        form = CreateTaskForm(initial={'priority': '2'})
        return render(request, "create_task_template.html", {"form": form})
