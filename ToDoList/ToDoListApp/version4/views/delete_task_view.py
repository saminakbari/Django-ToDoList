from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from ToDoListApp.models import Task, ToDoList
from ToDoListApp.serializers import TaskSerializer


class DeleteTaskView(LoginRequiredMixin, DestroyAPIView):
    serializer_class = TaskSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_destroy(self, instance):
        task = self.get_object()
        to_do_list = ToDoList.objects.get(pk=self.kwargs["list_id"])
        to_do_list.tasks.remove(task)
        return Response("Task deleted from list successfully.")
