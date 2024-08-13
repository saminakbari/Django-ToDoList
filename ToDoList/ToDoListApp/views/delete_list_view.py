from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.models import ToDoList2


@login_required
def delete_list(request, list_id):
    to_do_list = ToDoList2.objects.get(pk=list_id)
    to_do_list.delete()
    user = request.user
    return render(request, "show_all_lists_template.html",
                  {"to_do_lists": user.to_do_lists.all(), "username": user.username,
                   "message": "List deleted successfully."})
