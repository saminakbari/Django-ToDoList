from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from ToDoListApp.models import Task
from ToDoListApp.models.task import get_priority, get_state
from ToDoListApp.serializers import TaskSerializer


class GetTaskView(LoginRequiredMixin, RetrieveAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        result = {
            "title": task.title,
            "description": task.description,
            "deadline": task.deadline,
            "priority": get_priority(task.priority),
            "state": get_state(task.state)
        }
        if task.attachment:
            result["attachment"] = task.attachment
        else:
            result["attachment"] = "no attachment"
        return Response(result)
