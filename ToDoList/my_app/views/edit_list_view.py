from django.http import HttpResponse
from django.shortcuts import render, redirect

from my_app.models import ToDoList, MyUser


def edit_to_do_list(request, list_id, username):
    to_do_list = ToDoList.objects.get(pk=list_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        to_do_list.title = title
        to_do_list.save()
        user = MyUser.objects.get(username=username)
        return render(request, "show_all_lists_template.html",
                      {"to_do_lists": user.to_do_lists.all(), "username": username,
                       "message": "List edited successfully."})
    else:
        return render(request, "edit_list_title_template.html", {'to_do_list': to_do_list})
