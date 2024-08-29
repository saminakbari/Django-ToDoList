from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class ShareTaskView(APIView):
    serializer_class = TaskSerializer

    def post(self, request, **kwargs):
        username = self.request.data["username"]
        user = get_object_or_404(User.objects, username=username)
        user_tasks = Task.objects.filter(owner=self.request.user)
        task = user_tasks.get(pk=self.kwargs["pk"])
        user.tasks_shared_with_user.add(task)
        return Response("Task shared successfully.", status=200)
