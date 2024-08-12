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
            return render(request, "share_task_template.html",
                          {"message": "Username does not exist"})

        if task in receiver_user.tasks_shared_with_user.all():
            render(request, "share_task_template.html",
                   {"message": "You have already shared this task with this user."})

        receiver_user.tasks_shared_with_user.add(task)
        return render(request, "share_task_template.html", {"message": "Task is shared successfully."})

    else:
        return render(request, "share_task_template.html")
