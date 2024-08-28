from rest_framework.generics import RetrieveUpdateAPIView

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class EditTaskView(RetrieveUpdateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
