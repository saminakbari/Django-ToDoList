from django.shortcuts import render, redirect
from django.views import View

from ToDoListApp.models import MyUser


class Login(View):
    def get(self, request):
        return render(request, "v2_login_template.html",)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = MyUser.objects.get(username=username)
            if user.password != password:
                return render(request, "v2_login_template.html", {'message': 'Wrong password.'})
            return redirect("http://localhost:8000/v2/to-do-list/showall/" + username + "/")
        except MyUser.DoesNotExist:
            return render(request, "v2_login_template.html", {'message': 'Username does not exist.'})
