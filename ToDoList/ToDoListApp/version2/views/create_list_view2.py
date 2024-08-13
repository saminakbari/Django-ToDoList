from django.shortcuts import render
from django.views import View

from ToDoListApp.forms import CreateListForm
from ToDoListApp.models import MyUser, ToDoList


class CreateList(View):
    def get(self, request, username):
        form = CreateListForm()
        return render(request, 'v2_create_list_template.html', {"form": form})

    def post(self, request, username):
        form = CreateListForm(request.POST)
        if form.is_valid():
            title = form.get_title()
            user = MyUser.objects.get(username=username)
            to_do_list = ToDoList(title=title, owner=user)
            to_do_list.save()
            user = MyUser.objects.get(username=username)
            return render(request, "v2_show_all_lists_template.html",
                          {"to_do_lists": user.to_do_lists.all(), "username": username,
                           "message": "List created successfully."})