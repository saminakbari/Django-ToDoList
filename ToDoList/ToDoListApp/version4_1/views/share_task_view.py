from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class ShareTaskView(RetrieveUpdateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_update(self, serializer):
        username = self.request.data["username"]
        user = User.objects.get(username=username)
        task = self.get_object()
        user.tasks_shared_with_user.add(task)
        return Response("Task shared successfully.")
