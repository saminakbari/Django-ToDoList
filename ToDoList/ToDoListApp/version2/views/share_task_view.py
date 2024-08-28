from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from ToDoListApp.models import Task


class ShareTaskView(View):
    def get(self, request, task_id, list_id):
        return render(request, "v2/v2_share_task_template.html", {"list_id": list_id})

    def post(self, request, task_id, list_id):
        task = Task.objects.get(pk=task_id)
        receiver_username = request.POST.get("receiver_username")
        try:
            receiver_user = User.objects.get(username=receiver_username)
        except User.DoesNotExist:
            messages.add_message(request, messages.ERROR, "Username does not exist")
            return render(
                request, "v2/v2_share_task_template.html", {"list_id": list_id}
            )

        if task in receiver_user.tasks_shared_with_user.all():
            messages.add_message(
                request,
                messages.ERROR,
                "You have already shared this task with this user.",
            )
            render(request, "v2/v2_share_task_template.html", {"list_id": list_id})

        receiver_user.tasks_shared_with_user.add(task)
        messages.add_message(request, messages.INFO, "Task is shared successfully.")
        return render(request, "v2/v2_share_task_template.html", {"list_id": list_id})
