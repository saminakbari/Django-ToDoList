from django.http import HttpResponse
from django.shortcuts import render

from my_app.models.user import MyUser


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            MyUser.objects.get(username=username)
        except:
            user = MyUser(username=username, password=password)
            user.save()
            html = "<html><body>You are registered successfully.</body></html>"
            # return HttpResponse(html)
            return render(request, "login_template.html",
                          {'message': 'You''re registered successfully. Please login to continue.'})
        else:
            # return HttpResponse("<html><body>Username already exists.</body></html>")
            return render(request, "register_template.html", {'message': 'Username already exists.'})
    else:
        return render(request, "register_template.html")
