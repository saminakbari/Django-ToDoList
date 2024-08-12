from django.shortcuts import render

from my_app.forms.create_list_form import CreateListForm
from my_app.models import ToDoList, MyUser


def create_list(request):
    if request.method == 'POST':
        form = CreateListForm(request.POST)
        if form.is_valid():
            title = form.get_title()
            user = request.user
            to_do_list = ToDoList(title=title, owner=user)
            to_do_list.save()
            return render(request, "show_all_lists_template.html",
                          {"to_do_lists": user.to_do_lists.all(), "username": user.username,
                           "message": "List created successfully."})
    else:
        form = CreateListForm()
        return render(request, 'create_list_template.html', {"form": form})
