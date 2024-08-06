from django.shortcuts import redirect, render


def register_or_login(request):
    if request.method == 'POST':
        if request.POST.get('choice_button') == 'Sign up':
            return redirect("http://localhost:8000/user/register/")
        else:
            return redirect("http://localhost:8000/user/login/")
    else:
        return render(request, "register_login_template.html")
