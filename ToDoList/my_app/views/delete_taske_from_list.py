from django.http import HttpResponse

from my_app.models import Task, ToDoList


def delete_task_from_list(request, task_id, list_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        html = "<html><body>No task with this id was found.</body></html>"
        return HttpResponse(html)
    try:
        to_do_list = ToDoList.objects.get(id=list_id)
    except Task.DoesNotExist:
        html = "<html><body>No list with this id was found.</body></html>"
        return HttpResponse(html)

    if task in to_do_list.tasks.all():
        to_do_list.tasks.remove(task)
        to_do_list.save()
        html = "<html><body>Task removed from list successfully.</body></html>"
        return HttpResponse(html)
    else:
        html = "<html><body>The task does not exist in this list.</body></html>"
        return HttpResponse(html)
