from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from ToDoListApp.models import Task, ToDoList


class EditTask(LoginRequiredMixin, View):
    def get(self, request, list_id, task_id):
        task = Task.objects.get(pk=task_id)
        return render(request, "v2/v2_edit_task_template.html", {"task": task})

    def post(self, request, list_id, task_id):
        task = Task.objects.get(pk=task_id)
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.deadline = request.POST.get('deadline')
        task.priority = request.POST.get('priority')
        task.save()
        to_do_list = ToDoList.objects.get(pk=list_id)
        sorted_tasks = to_do_list.tasks.all().order_by('deadline', 'priority')
        return render(request, "v2/v2_get_list_template.html",
                      {"tasks": sorted_tasks, "to_do_list": to_do_list,
                       "user": to_do_list.owner, "message": "Task edited successfully."})
