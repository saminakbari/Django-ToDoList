from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.response import Response

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class GetTask4(LoginRequiredMixin, generics.RetrieveAPIView):
    serializer_class = TaskSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        result = {
            "title": task.title,
            "description": task.description,
            "deadline": task.deadline,
            "priority": task.priority,
        }
        if task.attachment:
            result["attachment"] = task.attachment
        else:
            result["attachment"] = "no attachment"
        return Response(result)
