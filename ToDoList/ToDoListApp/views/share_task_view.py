from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from ToDoListApp.models import Task, ToDoList


@login_required
def share_task(request, task_id, list_id):
    to_do_list = ToDoList.objects.get(pk=list_id)
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)
        receiver_username = request.POST.get('receiver_username')
        try:
            receiver_user = User.objects.get(username=receiver_username)
        except User.DoesNotExist:
            messages.add_message(request, messages.INFO, "Username does not exist")
            return render(request, "v1/share_task_template.html", {'to_do_list': to_do_list})

        if task in receiver_user.tasks_shared_with_user.all():
            messages.add_message(request, messages.INFO,
                                 "You have already shared this task with this user.")
            return render(request, "v1/share_task_template.html", {'to_do_list': to_do_list})

        receiver_user.tasks_shared_with_user.add(task)
        messages.add_message(request, messages.INFO, "Task is shared successfully.")
        return render(request, "v1/share_task_template.html", {'to_do_list': to_do_list})

    else:
        return render(request, "v1/share_task_template.html", {'to_do_list': to_do_list})
