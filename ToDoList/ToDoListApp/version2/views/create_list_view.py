from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from ToDoListApp.forms import ListForm
from ToDoListApp.models import ToDoList


class CreateList(LoginRequiredMixin, View):
    def get(self, request):
        form = ListForm()
        return render(request, "v2/v2_create_list_template.html", {"form": form})

    def post(self, request):
        form = ListForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            user = request.user
            to_do_list = ToDoList(title=title, owner=user)
            to_do_list.save()
            messages.add_message(request, messages.INFO, "List created successfully.")
            return render(
                request,
                "v2/v2_show_all_lists_template.html",
                {"to_do_lists": user.to_do_lists.all()},
            )

        else:
            errors = form.errors
            for error in errors:
                messages.add_message(request, messages.ERROR, error)
            form = ListForm()
            return render(request, "v2/v2_create_list_template.html", {"form": form})
