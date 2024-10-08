from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class DeleteTaskView(DestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_destroy(self, instance):
        task = self.get_object()
        to_do_list = self.request.user.to_do_lists.get(pk=self.request.data["list_id"])
        to_do_list.tasks.remove(task)
        return Response("Task deleted from list successfully.", status=200)
