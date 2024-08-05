from django.contrib.auth.models import User
from django.http import HttpResponse

# from my_app.models import MyUser


def register_user(request, username, password):
    user = User.objects.create_user(username=username, password=password)
    user.save()
    html = "<html><body>You are registered successfully.</body></html>"
    return HttpResponse(html)
