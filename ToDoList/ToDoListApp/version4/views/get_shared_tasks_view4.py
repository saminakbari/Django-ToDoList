from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class GetSharedTasks4(LoginRequiredMixin, generics.ListAPIView):
    model = Task
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.tasks_shared_with_user.all()
