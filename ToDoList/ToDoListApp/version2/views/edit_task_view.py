from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from ToDoListApp.forms import TaskForm
from ToDoListApp.models import Task, ToDoList


class EditTaskView(LoginRequiredMixin, View):
    def get(self, request, list_id, task_id):
        task = Task.objects.get(pk=task_id)
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
            request, "v2/v2_edit_task_template.html", {"task": task, "form": form}
        )

    def post(self, request, list_id, task_id):
        form = TaskForm(request.POST)
        task = Task.objects.get(pk=task_id)
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
            to_do_list = ToDoList.objects.get(pk=list_id)
            sorted_tasks = to_do_list.tasks.all().order_by("deadline", "priority")
            return render(
                request,
                "v2/v2_get_list_template.html",
                {
                    "tasks": sorted_tasks,
                    "to_do_list": to_do_list,
                    "user": to_do_list.owner,
                    "message": "Task edited successfully.",
                },
            )

        else:
            errors = form.errors.items()
            for error in errors:
                messages.add_message(request, messages.ERROR, error)
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
                request, "v2/v2_edit_task_template.html", {"task": task, "form": form}
            )
