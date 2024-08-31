from django.contrib import messages
from django.shortcuts import render

from ToDoListApp.forms import ListForm
from ToDoListApp.models import ToDoList


def edit_list_view(request, list_id):
    to_do_list = ToDoList.objects.get(pk=list_id)
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            message_text = "List edited successfully."
            title = form.cleaned_data["title"]
            if title:
                to_do_list.title = title
            else:
                message_text = "No change. You did not enter a new title."
            to_do_list.save()
            user = request.user
            messages.add_message(request, messages.INFO, message_text)
            return render(
                request,
                "v1/show_all_lists_template.html",
                {"to_do_lists": user.to_do_lists.all()},
            )
        else:
            errors = form.errors.items()
            for error in errors:
                messages.add_message(request, messages.ERROR, error[1])
    else:
        form = ListForm(initial={"title": to_do_list.title})
        return render(
            request,
            "v1/edit_list_title_template.html",
            {"to_do_list": to_do_list, "form": form},
        )
