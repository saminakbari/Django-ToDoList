from django.shortcuts import render
from django.views import View


class ShowListsView(View):
    def get(self, request):
        user = request.user
        to_do_lists = user.to_do_lists.all()
        return render(
            request, "v2/v2_show_all_lists_template.html", {"to_do_lists": to_do_lists}
        )
