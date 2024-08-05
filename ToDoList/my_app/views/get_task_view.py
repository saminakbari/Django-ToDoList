from django.http import HttpResponse
from django.shortcuts import render

from my_app.forms import GetTaskForm
from my_app.models import Task


def get_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return HttpResponse("<html><body>No such task</body></html>")

    html = ("<html><body> %s <br> description: %s <br> deadline %s <br> priority: %s</body></html>"
            % (task.title, task.description, str(task.deadline), task.priority))

    return HttpResponse(html)

# def get_task(request):
#     if request.method == 'POST':
#         form = GetTaskForm(request.POST)
#         if form.is_valid():
#             task_id = form.cleaned_data['task_id']
#             try:
#                 task = Task.objects.get(pk=task_id)
#             except Task.DoesNotExist:
#                 return HttpResponse("<html><body>No such task</body></html>")
#
#             html = ("<html><body> %s <br> description: %s <br> deadline %s <br> priority: %s</body></html>"
#                     % (task.title, task.description, str(task.deadline), task.priority))
#             return HttpResponse(html)
#
#     else:
#         form = GetTaskForm()
#         return render(request, "get_task_template.html", {'form': form})
