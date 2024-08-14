from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages

from ToDoListApp.forms.create_list_form import CreateListForm
from ToDoListApp.models import ToDoList2


@login_required
def create_list(request):
    if request.method == 'POST':
        form = CreateListForm(request.POST)
        if form.is_valid():
            title = form.get_title()
            user = request.user
            to_do_list = ToDoList2(title=title, owner=user)
            to_do_list.save()
            messages.add_message(request, messages.INFO, "List created successfully.")
            return render(request, "show_all_lists_template.html",
                          {"to_do_lists": user.to_do_lists.all(),
                           "username": user.username})
        else:
            errors = form.errors.items()
            for error in errors:
                messages.add_message(request, messages.ERROR, error[1][0])

    form = CreateListForm()
    return render(request, 'create_list_template.html', {"form": form})
