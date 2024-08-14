from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.forms import ListForm
from ToDoListApp.models import ToDoList2


@login_required
def get_list(request, list_id):
    to_do_list = ToDoList2.objects.get(pk=list_id)
    sorted_tasks = to_do_list.tasks.all().order_by('deadline', 'priority')
    return render(
        request,
        "get_list_template.html",
        {"tasks": sorted_tasks, "to_do_list": to_do_list,
         "user": to_do_list.owner},
    )
