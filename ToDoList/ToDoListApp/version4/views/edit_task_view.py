from rest_framework.generics import UpdateAPIView

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class EditTaskView(UpdateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
