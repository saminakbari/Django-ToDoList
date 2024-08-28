from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from ToDoListApp.models import ToDoList


class GetListView(LoginRequiredMixin, View):
    def get(self, request, list_id):
        to_do_list = ToDoList.objects.get(pk=list_id)

        sorted_tasks = to_do_list.tasks.all().order_by("deadline", "priority")

        return render(
            request,
            "v2/v2_get_list_template.html",
            {"tasks": sorted_tasks, "to_do_list": to_do_list, "user": to_do_list.owner},
        )
