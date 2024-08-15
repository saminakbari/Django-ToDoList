from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import UpdateView

from ToDoListApp.models.to_do_list import ToDoList


class EditList3(LoginRequiredMixin, UpdateView):
    template_name = "v3/v3_edit_list_title_template.html"
    fields = ["title"]
    model = ToDoList
    pk_url_kwarg = 'list_id'
    success_url = 'ToDoListApp.version3.urls.v3_urlpatterns.show_lists'
    # success_url = reverse('v3-edit-list')
