from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class ShowLists3(LoginRequiredMixin, TemplateView):
    template_name = "v3_show_all_lists_template.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["to_do_lists"] = user.to_do_lists.all()
        return context
