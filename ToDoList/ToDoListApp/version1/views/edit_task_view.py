from django.contrib import messages
from django.shortcuts import render

from ToDoListApp.forms import TaskForm
from ToDoListApp.models import Task, ToDoList


def edit_task_view(request, task_id, list_id):
    task = Task.objects.get(pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data["title"]
            task.description = form.cleaned_data["description"]
            task.deadline = form.cleaned_data["deadline"]
            task.priority = form.cleaned_data["priority"]

            if hasattr(request, "FILES") and "attachment" in request.FILES:
                file = request.FILES["attachment"]
                task.attachment = file

            if (
                "attachment-clear" in form.data
                and form.data["attachment-clear"] == "on"
            ):
                task.attachment.delete()

            task.save()
            messages.add_message(request, messages.INFO, "Task edited successfully.")

        else:
            errors = form.errors.items()
            for error in errors:
                messages.add_message(request, messages.ERROR, error[1])

        to_do_list = ToDoList.objects.get(pk=list_id)
        sorted_tasks = to_do_list.tasks.all().order_by("deadline", "priority")
        return render(
            request,
            "v1/get_list_template.html",
            {"tasks": sorted_tasks, "to_do_list": to_do_list, "user": to_do_list.owner},
        )

    else:
        form = TaskForm(
            initial={
                "title": task.title,
                "description": task.description,
                "deadline": task.deadline,
                "priority": task.priority,
                "attachment": task.attachment,
            }
        )
        return render(
            request, "v1/edit_task_template.html", {"task": task, "form": form}
        )
