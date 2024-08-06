from django.http import HttpResponse
from django.shortcuts import render

from my_app.models import ToDoList


def get_list(request, list_id):
    if request.method == 'GET':
        try:
            to_do_list = ToDoList.objects.get(pk=list_id)
        except ToDoList.DoesNotExist:
            return HttpResponse("<html><body>To-do list not found</body></html>")

        sorted_tasks = sorted(to_do_list.tasks.all(), key=lambda x: x.deadline)
        sorted_tasks = sorted(sorted_tasks, key=lambda x: x.priority)

        return render(request, "get_list_template.html",
                      {"tasks": sorted_tasks, "list_id": list_id,
                       "username": to_do_list.owner.username})
