from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def show_all_lists(request):
    user = request.user
    to_do_lists = user.to_do_lists.all()
    return render(request, "v1/show_all_lists_template.html",
                  {"to_do_lists": to_do_lists, "username": user.username})
