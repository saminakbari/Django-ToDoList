from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from ToDoListApp.models import Task, ToDoList


class AddSharedTasks(LoginRequiredMixin, View):
    def get(self, request, username, list_id):
        user = User.objects.get(username=username)
        to_do_list = ToDoList.objects.get(list_id=list_id)
        shared_tasks = user.tasks_shared_with_user.all()
        return render(request, "v2_add_shared_tasks_template.html",
                      {'tasks': shared_tasks, 'user': user, 'to_do_list': to_do_list})

    def post(self, request, username, list_id):
        user = User.objects.get(username=username)
        to_do_list = ToDoList.objects.get(list_id=list_id)
        shared_tasks = user.tasks_shared_with_user.all()
        task_id = request.POST.get('task_id')
        task = Task.objects.get(task_id=task_id)
        to_do_list.tasks.add(task)
        return render(request, "v2_add_shared_tasks_template.html",
                      {'tasks': shared_tasks, 'user': user, 'to_do_list': to_do_list})
