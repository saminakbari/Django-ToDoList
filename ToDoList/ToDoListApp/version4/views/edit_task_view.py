from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import RetrieveUpdateAPIView

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class EditTask(LoginRequiredMixin, RetrieveUpdateAPIView):
    serializer_class = TaskSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
