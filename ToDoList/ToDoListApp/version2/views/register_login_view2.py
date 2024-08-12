from django.shortcuts import render, redirect
from django.views import View


class RegisterLogin(View):
    def get(self, request, *args, **kwargs):
        return render(request, "v2_register_login_template.html")

    def post(self, request, *args, **kwargs):
        if request.POST.get('choice_button') == 'Sign up':
            return redirect("http://localhost:8000/v2/user/register/")
        else:
            return redirect("http://localhost:8000/v2/user/login/")
