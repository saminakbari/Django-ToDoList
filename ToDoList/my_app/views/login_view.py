from django.contrib.auth import login
# from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from my_app.models import MyUser


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = MyUser.objects.get(username=username)
            if user.password != password:
                return HttpResponse("<html><body>Wrong password.</body></html>")
            return redirect("http://localhost:8000/to-do-list/showall/" + username + "/")
        except MyUser.DoesNotExist:
            return HttpResponse("<html><body>Username does not exist.</body></html>")

    else:
        return render(request, "login_template.html")
