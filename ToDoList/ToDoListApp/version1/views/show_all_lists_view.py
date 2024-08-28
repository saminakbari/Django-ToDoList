from django.shortcuts import render


def show_all_lists_view(request):
    user = request.user
    to_do_lists = user.to_do_lists.all()
    return render(
        request, "v1/show_all_lists_template.html", {"to_do_lists": to_do_lists}
    )
