from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.models import ToDoList2


@login_required
def edit_list(request, list_id):
    to_do_list = ToDoList2.objects.get(pk=list_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        to_do_list.title = title
        to_do_list.save()
        user = request.user
        messages.add_message(request, messages.INFO, "List edited successfully.")
        return render(request, "show_all_lists_template.html",
                      {"to_do_lists": user.to_do_lists.all(), "username": user.username})
    else:
        return render(request, "edit_list_title_template.html",
                      {'to_do_list': to_do_list})
