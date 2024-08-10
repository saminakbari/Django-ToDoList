from django.shortcuts import redirect, render

from my_app.models import MyUser


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = MyUser.objects.get(username=username)
            if user.password != password:
                # return HttpResponse("<html><body>Wrong password.</body></html>")
                return render(request, "login_template.html", {'message': "Wrong password."})
            return redirect("http://localhost:8000/to-do-list/showall/" + username + "/")
        except MyUser.DoesNotExist:
            # return HttpResponse("<html><body>Username does not exist.</body></html>")
            return render(request, "login_template.html", {'message': "Username does not exist."})

    else:
        return render(request, "login_template.html")
