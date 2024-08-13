from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.models import MyUser, Task


@login_required
def share_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)
        receiver_username = request.POST.get('receiver_username')
        try:
            receiver_user = MyUser.objects.get(username=receiver_username)
        except MyUser.DoesNotExist:
            messages.add_message(request, messages.INFO, "Username does not exist")
            return render(request, "share_task_template.html")

        if task in receiver_user.tasks_shared_with_user.all():
            messages.add_message(request, messages.INFO,
                                 "You have already shared this task with this user.")
            return render(request, "share_task_template.html")

        receiver_user.tasks_shared_with_user.add(task)
        messages.add_message(request, messages.INFO, "Task is shared successfully.")
        return render(request, "share_task_template.html")

    else:
        return render(request, "share_task_template.html")
