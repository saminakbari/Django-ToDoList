from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.forms.create_task_form import CreateTaskForm
from ToDoListApp.models import Task2, ToDoList2


@login_required
def create_task(request, list_id):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = ''
            if form.data['description']:
                description = form.cleaned_data['description']
            deadline = form.cleaned_data['deadline']
            priority = form.cleaned_data['priority']
            task = Task2(title=title, description=description, deadline=deadline, priority=priority)
            task.save()
            to_do_list = ToDoList2.objects.get(pk=list_id)
            task.to_do_lists.add(to_do_list)
            task.owner = to_do_list.owner
            task.save()
            sorted_tasks = to_do_list.tasks.all().order_by('deadline', 'priority')
            return render(request, "get_list_template.html",
                          {"tasks": sorted_tasks, "to_do_list": to_do_list,
                           "user": to_do_list.owner, "message": "Task created successfully."})

    else:
        form = CreateTaskForm(initial={'priority': '2'})
        return render(request, "create_task_template.html", {"form": form})
