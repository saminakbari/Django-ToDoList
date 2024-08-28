from django.views.generic import TemplateView


class ShowListsView(TemplateView):
    template_name = "v3/v3_show_all_lists_template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["to_do_lists"] = user.to_do_lists.all()
        return context
