from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from my_app.models import MyUser


class Register(View):
    def get(self, request):
        return render(request, "register_template.html")

    def post(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            try:
                MyUser.objects.get(username=username)
            except:
                user = MyUser(username=username, password=password)
                user.save()
                html = "<html><body>You are registered successfully.</body></html>"
                return HttpResponse(html)
            else:
                return HttpResponse("<html><body>Username already exists.</body></html>")
