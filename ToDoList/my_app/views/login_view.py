from django.contrib.auth import login
# from django.contrib.auth.models import User
from django.http import HttpResponse


def login_user(request, username, password):
    pass
    #try:
    #     user = User.objects.get(username=username)
    #     try:
    #         login(request, user)
    #         # redirect
    #     except:
    #         return HttpResponse("<html><body>Wrong password.</body></html>")
    # except User.DoesNotExist:
    #     return HttpResponse("<html><body>User does not exist.</body></html>")
