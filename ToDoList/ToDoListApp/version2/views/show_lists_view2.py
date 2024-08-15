from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View


class ShowLists(LoginRequiredMixin, View):
    def get(self, request, username):
        user = User.objects.get(username=username)
        to_do_lists = user.to_do_lists.all()
        return render(request, "v2_show_all_lists_template.html",
                      {"to_do_lists": to_do_lists, "username": username})
