from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.forms.task_form import TaskForm
from ToDoListApp.models import Task2, ToDoList2


@login_required
def create_task(request, list_id):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            description = ''
            if form.cleaned_data['description']:
                description = form.cleaned_data['description']
            title = form.cleaned_data['title']
            deadline = form.cleaned_data['deadline']
            priority = form.cleaned_data['priority']
            to_do_list = ToDoList2.objects.get(pk=list_id)
            task = Task2.objects.create(description=description, priority=priority, owner=to_do_list.owner)

            try:
                file = request.FILES['attachment']
                task.attachment = file
            except:
                pass

            if title:
                task.title = title
            if deadline:
                task.deadline = deadline
            task.save()
            task.to_do_lists.add(to_do_list)
            sorted_tasks = to_do_list.tasks.all().order_by('deadline', 'priority')
            messages.add_message(request, messages.INFO, "Task created successfully.")
            return render(request, "get_list_template.html",
                          {"tasks": sorted_tasks, "to_do_list": to_do_list,
                           "user": to_do_list.owner})
        else:
            errors = form.errors.items()
            for error in errors:
                messages.add_message(request, messages.ERROR, error[1][0])

    form = TaskForm(initial={'priority': '2'})
    return render(request, "create_task_template.html", {"form": form})
