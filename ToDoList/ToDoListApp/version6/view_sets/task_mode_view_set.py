from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets


class TaskModelViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    pass
