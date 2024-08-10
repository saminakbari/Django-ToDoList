from django.shortcuts import render, redirect

from my_app.models import ToDoList, MyUser
from django.http import HttpResponse


def delete_list(request, list_id, username):
    to_do_list = ToDoList.objects.get(pk=list_id)
    to_do_list.delete()
    # return redirect(to="http://localhost:8000/to-do-list/showall/" + username + "/")
    user = MyUser.objects.get(username=username)
    return render(request, "show_all_lists_template.html",
                  {"to_do_lists": user.to_do_lists.all(), "username": username,
                   "message": "List deleted successfully."})
