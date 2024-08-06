from django.http import HttpResponse
from django.shortcuts import render

from my_app.models import Task


def edit_task(request, task_id, username):
    if request.method == 'GET':
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return HttpResponse("<html><body>Task not found</body></html>")
        if task.owner.username == username:
            return render(request, "edit_task_template.html", {"task": task})
        else:
            return HttpResponse("<html><body>You don't have permission to edit a task that has been shared with "
                                "you.</body></html>")

    else:
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return HttpResponse("<html><body>Task not found</body></html>")

        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.deadline = request.POST.get('deadline')
        task.priority = request.POST.get('priority')
        task.save()
        html = "<html><body>Task updated successfully.</body></html>"
        return HttpResponse(html)
