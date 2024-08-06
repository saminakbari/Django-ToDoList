from django.shortcuts import render
from django.http import HttpResponse

from my_app.models import MyUser, Task, ToDoList


def show_shared_tasks(request, username, list_id):
    user = MyUser.objects.get(username=username)
    if request.method == 'POST':
        pressed_value = request.POST.get('add')
        pressed_value = pressed_value.replace('Add task ', '')
        task_id = int(pressed_value)
        task = Task.objects.get(task_id=task_id)
        to_do_list = ToDoList.objects.get(list_id=list_id)
        to_do_list.tasks.add(task)
        user.tasks_shared_with_user.remove(task)
        return HttpResponse("<html><body>The task added successfully.</body></html>")
    else:
        shared_tasks = user.tasks_shared_with_user.all()
        return render(request, "add_shared_tasks_template.html",
                      {'tasks': shared_tasks, 'username': username})
