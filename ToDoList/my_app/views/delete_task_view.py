from django.http import HttpResponse
from django.shortcuts import render

from my_app.forms import DeleteTaskForm
from my_app.models import Task


def delete_task(request, task_id: int):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
        html = "<html><body>The task deleted successfully.</body></html>"
        return HttpResponse(html)
    except Task.DoesNotExist:
        html = "<html><body>The task does not exist.</body></html>"
        return HttpResponse(html)

# def delete_task(request):
#     if request.method == 'POST':
#         form = DeleteTaskForm(request.POST)
#         if form.is_valid():
#             task_id = form.cleaned_data['task_id']
#             try:
#                 task = Task.objects.get(pk=task_id)
#                 task.delete()
#                 html = "<html><body>The task deleted successfully.</body></html>"
#                 return HttpResponse(html)
#             except Task.DoesNotExist:
#                 html = "<html><body>The task does not exist.</body></html>"
#                 return HttpResponse(html)
#
#     else:
#         form = DeleteTaskForm()
#         return render(request, "delete_task_template.html", {"form": form})
