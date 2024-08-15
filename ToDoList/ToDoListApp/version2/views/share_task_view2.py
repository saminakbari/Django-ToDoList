from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from ToDoListApp.models import Task


class ShareTask(LoginRequiredMixin, View):
    def get(self, request, task_id):
        return render(request, "v2/v2_share_task_template.html")

    def post(self, request, task_id):
        task = Task.objects.get(pk=task_id)
        receiver_username = request.POST.get('receiver_username')
        try:
            receiver_user = User.objects.get(username=receiver_username)
        except User.DoesNotExist:
            return render(request, "v2/v2_share_task_template.html",
                          {"message": "Username does not exist"})

        if task in receiver_user.tasks_shared_with_user.all():
            render(request, "v2/v2_share_task_template.html",
                   {"message": "You have already shared this task with this user."})

        receiver_user.tasks_shared_with_user.add(task)
        return render(request, "v2/v2_share_task_template.html",
                      {"message": "Task is shared successfully."})
