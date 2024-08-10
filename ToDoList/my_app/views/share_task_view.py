from django.http import HttpResponse
from django.shortcuts import render

from my_app.models import MyUser, Task


def share_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        receiver_username = request.POST.get('receiver_username')
        try:
            receiver_user = MyUser.objects.get(username=receiver_username)
        except MyUser.DoesNotExist:
            # return HttpResponse("<html><body>Username does not exist.</body></html>")
            return render(request, "share_task_template.html",
                          {"message": "Username does not exist"})

        if task in receiver_user.tasks_shared_with_user.all():
            # return HttpResponse("<html><body>You have already shared this task with this user.</body></html>")
            render(request, "share_task_template.html",
                   {"message": "You have already shared this task with this user."})

        receiver_user.tasks_shared_with_user.add(task)
        # return HttpResponse("<html><body>Task shared successfully.</body></html>")
        return render(request, "share_task_template.html", {"message": "Task is shared successfully."})

    else:
        return render(request, "share_task_template.html")