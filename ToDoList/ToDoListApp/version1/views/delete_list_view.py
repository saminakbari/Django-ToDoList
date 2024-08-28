from django.contrib import messages
from django.shortcuts import render

from ToDoListApp.models import ToDoList


def delete_list_view(request, list_id):
    to_do_list = ToDoList.objects.get(pk=list_id)
    to_do_list.delete()
    user = request.user
    messages.add_message(request, messages.INFO, "List deleted successfully.")
    return render(
        request,
        "v1/show_all_lists_template.html",
        {"to_do_lists": user.to_do_lists.all()},
    )
