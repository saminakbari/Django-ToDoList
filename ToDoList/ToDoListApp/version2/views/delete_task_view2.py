from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from ToDoListApp.models import Task, ToDoList


class DeleteTask(LoginRequiredMixin, View):
    def get(self, request, task_id, list_id):
        task = Task.objects.get(pk=task_id)
        to_do_list = ToDoList.objects.get(pk=list_id)
        to_do_list.tasks.remove(task)
        to_do_list.save()
        sorted_tasks = to_do_list.tasks.all().order_by('deadline', 'priority')
        return render(request, "v2_get_list_template.html",
                      {"tasks": sorted_tasks, "user": to_do_list.owner,
                       "message": "Task deleted successfully.", "to_do_list": to_do_list})
