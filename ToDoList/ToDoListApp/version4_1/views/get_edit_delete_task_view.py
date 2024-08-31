from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from ToDoListApp.serializers import TaskSerializer


class GetEditDeleteTaskView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.request.user.shared_added_tasks.all() | self.request.user.tasks.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context

    def perform_destroy(self, instance):
        task = self.get_object()
        to_do_list = self.request.user.to_do_lists.get(pk=self.request.data["list_id"])
        to_do_list.tasks.remove(task)
        return Response("Task deleted from list successfully.", status=200)
