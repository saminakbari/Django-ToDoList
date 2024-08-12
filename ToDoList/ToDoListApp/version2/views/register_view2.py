from django.shortcuts import redirect, render
from django.views import View

from ToDoListApp.models import MyUser


class Register(View):
    def get(self, request):
        return render(request, "v2_register_template.html")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            MyUser.objects.get(username=username)
        except MyUser.DoesNotExist:
            user = MyUser(username=username, password=password)
            user.save()
            return redirect("http://localhost:8000/v2/to-do-list/showall/" + username + "/")
        else:
            return render(request, "v2_register_template.html", {'message': 'Username already exists.'})
