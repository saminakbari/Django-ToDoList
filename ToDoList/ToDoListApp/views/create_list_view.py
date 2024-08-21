from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.forms.list_form import ListForm
from ToDoListApp.models import ToDoList


@login_required
def create_list(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            user = request.user
            to_do_list = ToDoList(owner=user)
            title = form.cleaned_data['title']
            if title:
                to_do_list.title = title
            to_do_list.save()
            messages.add_message(request, messages.INFO, "List created successfully.")
            return render(request, "v1/show_all_lists_template.html",
                          {"to_do_lists": user.to_do_lists.all()})
        else:
            errors = form.errors.items()
            for error in errors:
                messages.add_message(request, messages.ERROR, error[1])

    form = ListForm()
    return render(request, 'v1/create_list_template.html', {"form": form})
