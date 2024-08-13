from django.shortcuts import render
from django.views import View

from ToDoListApp.models import MyUser, ToDoList


class EditList(View):
    def get(self, request, list_id, username):
        to_do_list = ToDoList.objects.get(pk=list_id)
        return render(request, "v2_edit_list_title_template.html",
                      {'to_do_list': to_do_list})

    def post(self, request, list_id, username):
        to_do_list = ToDoList.objects.get(pk=list_id)
        title = request.POST.get('title')
        to_do_list.title = title
        to_do_list.save()
        user = MyUser.objects.get(username=username)
        return render(request, "v2_show_all_lists_template.html",
                      {"to_do_lists": user.to_do_lists.all(), "username": username,
                       "message": "List edited successfully."})
