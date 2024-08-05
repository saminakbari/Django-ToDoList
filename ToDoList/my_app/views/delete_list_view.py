from django.shortcuts import render

from my_app.forms import DeleteListForm
from my_app.models import ToDoList
from django.http import HttpResponse


def delete_list(request, list_id):
    try:
        to_do_list = ToDoList.objects.get(pk=list_id)
        to_do_list.delete()
        html = "<html><body>The to-do list deleted successfully.</body></html>"
        return HttpResponse(html)
    except ToDoList.DoesNotExist:
        html = "<html><body>The to-do list does not exist.</body></html>"
        return HttpResponse(html)

# def delete_list(request):
#     if request.method == 'POST':
#         form = DeleteListForm(request.POST)
#         if form.is_valid():
#             list_id = form.cleaned_data['list_id']
#             try:
#                 to_do_list = ToDoList.objects.get(pk=list_id)
#                 to_do_list.delete()
#                 html = "<html><body>The to-do list deleted successfully.</body></html>"
#                 return HttpResponse(html)
#             except ToDoList.DoesNotExist:
#                 html = "<html><body>The to-do list does not exist.</body></html>"
#                 return HttpResponse(html)
#     else:
#         form = DeleteListForm()
#         return render(request, "delete_list_template.html", {"form": form})
