from django.shortcuts import render

from ToDoListApp.models import Task, ToDoList


def add_shared_tasks_view(request, list_id):
    user = request.user
    to_do_list = ToDoList.objects.get(id=list_id)
    shared_tasks = user.tasks_shared_with_user.all()
    if request.method == "POST":
        task_id = request.POST.get("add")
        task = Task.objects.get(id=task_id)
        to_do_list.tasks.add(task)
        return render(
            request,
            "v1/add_shared_tasks_template.html",
            {"tasks": shared_tasks, "user": user, "to_do_list": to_do_list},
        )
    else:
        return render(
            request,
            "v1/add_shared_tasks_template.html",
            {"tasks": shared_tasks, "user": user, "to_do_list": to_do_list},
        )
