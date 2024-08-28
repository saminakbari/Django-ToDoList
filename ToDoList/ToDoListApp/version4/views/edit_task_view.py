from rest_framework.generics import UpdateAPIView

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class EditTaskView(UpdateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
