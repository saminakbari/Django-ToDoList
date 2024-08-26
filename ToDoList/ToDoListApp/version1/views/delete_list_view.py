from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.models import ToDoList


@login_required
def delete_list(request, list_id):
    to_do_list = ToDoList.objects.get(pk=list_id)
    to_do_list.delete()
    user = request.user
    messages.add_message(request, messages.INFO, "List deleted successfully.")
    return render(
        request,
        "v1/show_all_lists_template.html",
        {"to_do_lists": user.to_do_lists.all()},
    )
