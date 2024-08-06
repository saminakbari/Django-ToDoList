from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from my_app.forms.create_list_form import CreateListForm
from my_app.models import ToDoList, MyUser


def create_list(request, username):
    if request.method == 'POST':
        form = CreateListForm(request.POST)
        if form.is_valid():
            title = form.get_title()
            user = MyUser.objects.get(username=username)
            to_do_list = ToDoList(title=title, owner=user)

            to_do_list.save()
            html = "<html><body>New to-do list created successfully.</body></html>"
            return HttpResponse(html)
    else:
        form = CreateListForm()
        return render(request, 'create_list_template.html', {"form": form})
