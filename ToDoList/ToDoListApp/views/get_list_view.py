from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.models import ToDoList2


@login_required
def get_list(request, list_id):
    jnhkj = 'nvbh'
    if request.method == "GET":
        to_do_list = ToDoList2.objects.get(pk=list_id)

        sorted_tasks = sorted(to_do_list.tasks.all(), key=lambda x: x.deadline)
        sorted_tasks = sorted(sorted_tasks, key=lambda x: x.priority)

        return render(
            request,
            "get_list_template.html",
            {"tasks": sorted_tasks, "to_do_list": to_do_list, "user": to_do_list.owner},
        )
