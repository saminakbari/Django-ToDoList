from django.http import HttpResponse
from django.shortcuts import render

from my_app.models import ToDoList


def edit_to_do_list(request, list_id):
    try:
        to_do_list = ToDoList.objects.get(pk=list_id)
    except ToDoList.DoesNotExist:
        html = "<html><body>To-do list does not exist.</body></html>"
        return HttpResponse(html)

    if request.method == 'POST':
        title = request.POST.get('title')
        to_do_list.title = title
        to_do_list.save()
        html = "<html><body>To-do list updated successfully.</body></html>"
        return HttpResponse(html)

    else:
        return render(request, "edit_list_title_template.html", {'to_do_list': to_do_list})
