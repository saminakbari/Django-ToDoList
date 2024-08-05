from django.http import HttpResponse
from django.shortcuts import render

from my_app.forms import GetListForm
from my_app.models import ToDoList


def get_list(request, list_id):
    if request.method == 'GET':
        try:
            to_do_list = ToDoList.objects.get(pk=list_id)
        except ToDoList.DoesNotExist:
            return HttpResponse("<html><body>To-do list not found</body></html>")

        return render(request, "get_list_template.html", {"tasks": to_do_list.tasks.all()})
    # else:
    #     return render(request, "show_all_lists_template.html", {"to_do_lists": ToDoList.objects.all()})
