from django.shortcuts import render

from my_app.models import ToDoList


def show_all_lists(request):
    to_do_lists = ToDoList.objects.all()
    return render(request, "show_all_lists_template.html", {"to_do_lists": to_do_lists})
