from django.shortcuts import render, redirect

from my_app.models.user import MyUser


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            MyUser.objects.get(username=username)
        except MyUser.DoesNotExist:
            user = MyUser(username=username, password=password)
            user.save()
            return redirect("http://localhost:8000/to-do-list/showall/" + username + "/")
        else:
            return render(request, "register_template.html", {'message': 'Username already exists.'})
    else:
        return render(request, "register_template.html")
