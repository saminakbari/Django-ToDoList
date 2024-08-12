from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ToDoListApp.forms.create_list_form import CreateListForm
from ToDoListApp.models import ToDoList, ToDoList2


@login_required
def create_list(request):
    if request.method == 'POST':
        form = CreateListForm(request.POST)
        if form.is_valid():
            title = form.get_title()
            user = request.user
            to_do_list = ToDoList2(title=title, owner=user)
            to_do_list.save()
            return render(request, "show_all_lists_template.html",
                          {"to_do_lists": user.to_do_lists.all(), "username": user.username,
                           "message": "List created successfully."})
    else:
        form = CreateListForm()
        return render(request, 'create_list_template.html', {"form": form})
