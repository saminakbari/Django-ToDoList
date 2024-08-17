from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from ToDoListApp.forms import ListForm
from ToDoListApp.models import ToDoList


class EditList(LoginRequiredMixin, View):
    def get(self, request, list_id):
        to_do_list = ToDoList.objects.get(pk=list_id)
        form = ListForm(initial={'title': to_do_list.title})
        return render(request, "v2/v2_edit_list_title_template.html",
                      {'to_do_list': to_do_list, 'form': form})

    def post(self, request, list_id):
        form = ListForm(request.POST)
        to_do_list = ToDoList.objects.get(pk=list_id)
        if form.is_valid():
            title = form.cleaned_data['title']
            to_do_list.title = title
            to_do_list.save()
            user = request.user
            messages.add_message(request, messages.INFO, "List edited successfully.")
            return render(request, "v2/v2_show_all_lists_template.html",
                          {"to_do_lists": user.to_do_lists.all()})
        else:
            errors = form.errors.items()
            for error in errors:
                messages.add_message(request, messages.ERROR, error)
            form = ListForm(initial={'title': to_do_list.title})
            return render(request, "v2/v2_edit_list_title_template.html",
                          {'to_do_list': to_do_list, 'form': form})
