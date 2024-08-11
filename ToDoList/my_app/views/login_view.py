from django.shortcuts import redirect, render

from my_app.models import MyUser


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = MyUser.objects.get(username=username)
            if user.password != password:
                return render(request, "login_template.html", {'message': "Wrong password."})
            return redirect("http://localhost:8000/to-do-list/showall/" + username + "/")
        except MyUser.DoesNotExist:
            return render(request, "login_template.html", {'message': "Username does not exist."})

    else:
        return render(request, "login_template.html")
