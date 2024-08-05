from django.http import HttpResponse
from django.shortcuts import render

from my_app.models import Task


# def edit_task(request, task_id, **kwargs):
#     try:
#         task = Task.objects.get(pk=task_id)
#     except Task.DoesNotExist:
#         return HttpResponse("<html><body>Task not found</body></html>")
#
#     task.title = kwargs.get('title', task.title)
#     task.description = kwargs.get('description', task.description)
#     task.deadline = kwargs.get('deadline', task.deadline)
#     task.priority = kwargs.get('priority', task.priority)
#     task.save()
#
#     html = "<html><body>Task updated successfully.</body></html>"
#     return HttpResponse(html)


def edit_task(request, task_id):
    if request.method == 'GET':
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return HttpResponse("<html><body>Task not found</body></html>")

        return render(request, "edit_task_template.html", {"task": task})

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

# def edit_task(request):
#     if request.method == 'POST':
#         task_id = request.POST.get('task_id')
#         try:
#             task = Task.objects.get(pk=task_id)
#         except Task.DoesNotExist:
#             return HttpResponse("<html><body>Task not found</body></html>")
