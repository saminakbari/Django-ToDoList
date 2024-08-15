from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from ToDoListApp.models.to_do_list import ToDoList


class CreateList3(LoginRequiredMixin, CreateView):
    model = ToDoList
    fields = ["title"]
    template_name = "v3/v3_create_list_template.html"
    success_url = "'ToDoListApp.version3.urls.v3_urlpatterns.show_lists'"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateList3, self).form_valid(form)

