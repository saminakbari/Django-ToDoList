from django.shortcuts import render
from django.views import View

from ToDoListApp.models import ToDoList


class GetList(View):
    def get(self, request, list_id):
        to_do_list = ToDoList.objects.get(pk=list_id)

        sorted_tasks = sorted(to_do_list.tasks.all(), key=lambda x: x.deadline)
        sorted_tasks = sorted(sorted_tasks, key=lambda x: x.priority)

        return render(request, "v2_get_list_template.html",
                      {"tasks": sorted_tasks, "to_do_list": to_do_list, "user": to_do_list.owner})
