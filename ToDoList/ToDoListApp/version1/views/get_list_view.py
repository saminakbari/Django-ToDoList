from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.models import ToDoList


@login_required
def get_list(request, list_id):
    to_do_list = ToDoList.objects.get(pk=list_id)
    sorted_tasks = to_do_list.tasks.all().order_by("deadline", "priority")
    return render(
        request,
        "v1/get_list_template.html",
        {"tasks": sorted_tasks, "to_do_list": to_do_list, "user": to_do_list.owner},
    )
