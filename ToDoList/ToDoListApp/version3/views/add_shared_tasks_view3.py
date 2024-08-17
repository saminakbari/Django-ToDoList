from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class AddSharedTasks3(LoginRequiredMixin, TemplateView):
    pass
