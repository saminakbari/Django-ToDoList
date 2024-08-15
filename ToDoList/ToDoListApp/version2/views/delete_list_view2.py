from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from ToDoListApp.models import ToDoList


class DeleteList(LoginRequiredMixin, View):
    def get(self, request, list_id):
        to_do_list = ToDoList.objects.get(pk=list_id)
        to_do_list.delete()
        user = request.user
        return render(request, "v2/v2_show_all_lists_template.html",
                      {"to_do_lists": user.to_do_lists.all(), "username": user.username,
                       "message": "List deleted successfully."})
