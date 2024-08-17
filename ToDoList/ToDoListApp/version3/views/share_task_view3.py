from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class ShareTask3(LoginRequiredMixin, TemplateView):
    pass
