from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from ToDoListApp.models import Task, ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class AddSharedTask(LoginRequiredMixin, RetrieveUpdateAPIView):
    serializer_class = ToDoListSerializer
    lookup_field = "id"

    def get_queryset(self):
        return ToDoList.objects.filter(owner=self.request.user)

    def perform_update(self, serializer):
        task_id = self.request.data["task_id"]
        task = Task.objects.get(pk=task_id)
        to_do_list = self.get_object()
        to_do_list.tasks.add(task)
        return Response("Added.")
