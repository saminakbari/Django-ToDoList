from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from ToDoListApp.models import ToDoList


class EditList(LoginRequiredMixin, View):
    def get(self, request, list_id):
        to_do_list = ToDoList.objects.get(pk=list_id)
        return render(request, "v2/v2_edit_list_title_template.html",
                      {'to_do_list': to_do_list})

    def post(self, request, list_id):
        to_do_list = ToDoList.objects.get(pk=list_id)
        title = request.POST.get('title')
        to_do_list.title = title
        to_do_list.save()
        user = request.user
        messages.add_message(request, messages.INFO, "List edited successfully.")
        return render(request, "v2/v2_show_all_lists_template.html",
                      {"to_do_lists": user.to_do_lists.all()})
