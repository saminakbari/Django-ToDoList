from django.http import HttpResponse
from django.shortcuts import render

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
            return HttpResponse("<html><body>New task added to the to-do list successfully.</body></html>")

    else:
        form = CreateTaskForm()
        return render(request, "create_task_template.html", {"form": form})
