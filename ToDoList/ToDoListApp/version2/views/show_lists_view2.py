from django.shortcuts import render
from django.views import View

from ToDoListApp.models import MyUser


class ShowLists(View):
    def get(self, request, username):
        user = MyUser.objects.get(username=username)
        to_do_lists = user.to_do_lists.all()
        return render(request, "v2_show_all_lists_template.html",
                      {"to_do_lists": to_do_lists, "username": username})
