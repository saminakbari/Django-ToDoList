from django.shortcuts import render
from django.http import HttpResponse

from my_app.models import MyUser, Task, ToDoList


def show_shared_tasks(request, username, list_id):
    user = MyUser.objects.get(username=username)
    to_do_list = ToDoList.objects.get(list_id=list_id)
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = Task.objects.get(task_id=task_id)
        to_do_list.tasks.add(task)
        # return HttpResponse("<html><body>The task added successfully.</body></html>")

        sorted_tasks = sorted(to_do_list.tasks.all(), key=lambda x: x.deadline)
        sorted_tasks = sorted(sorted_tasks, key=lambda x: x.priority)
        return render(request, "get_list_template.html",
                      {"tasks": sorted_tasks, "list_id": list_id, "user": to_do_list.owner,
                       "message": "Task added successfully."})
    else:
        shared_tasks = user.tasks_shared_with_user.all()
        return render(request, "add_shared_tasks_template.html",
                      {'tasks': shared_tasks, 'user': user, 'to_do_list': to_do_list})

