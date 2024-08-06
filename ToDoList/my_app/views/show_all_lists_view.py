from django.shortcuts import render

from my_app.models import ToDoList, MyUser


def show_all_lists(request, username):
    user = MyUser.objects.get(username=username)
    to_do_lists = user.to_do_lists.all()

    return render(request, "show_all_lists_template.html",
                  {"to_do_lists": to_do_lists, "username": username})
