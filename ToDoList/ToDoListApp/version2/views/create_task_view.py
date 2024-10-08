from django.contrib import messages
from django.shortcuts import render
from django.views import View

from ToDoListApp.forms import TaskForm
from ToDoListApp.models import Task, ToDoList


class CreateTaskView(View):
    def get(self, request, list_id):
        form = TaskForm(initial={"priority": "2"})
        return render(request, "v2/v2_create_task_template.html", {"form": form})

    def post(self, request, list_id):
        form = TaskForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            deadline = form.cleaned_data["deadline"]
            priority = form.cleaned_data["priority"]
            to_do_list = ToDoList.objects.get(pk=list_id)
            task = Task(priority=priority, owner=to_do_list.owner)
            if title:
                task.title = title
            if deadline:
                task.deadline = deadline
            if description:
                task.description = description

            if hasattr(request, "FILES") and "attachment" in request.FILES:
                file = request.FILES
                task.attachment = file

            task.save()
            task.to_do_lists.add(to_do_list)

            sorted_tasks = to_do_list.tasks.all().order_by("deadline", "priority")
            messages.add_message(request, messages.INFO, "Task created successfully.")
            return render(
                request,
                "v2/v2_get_list_template.html",
                {
                    "tasks": sorted_tasks,
                    "to_do_list": to_do_list,
                    "user": to_do_list.owner,
                },
            )

        else:
            errors = form.errors.items()
            for error in errors:
                messages.add_message(request, messages.ERROR, error[1])
            form = TaskForm(initial={"priority": "2"})
            return render(request, "v2/v2_create_task_template.html", {"form": form})
