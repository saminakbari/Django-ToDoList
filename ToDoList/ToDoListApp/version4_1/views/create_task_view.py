from rest_framework.generics import CreateAPIView

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class CreateTaskView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        to_do_list = self.request.user.to_do_lists.get(pk=self.request.data["list_id"])
        context["to_do_list"] = to_do_list
        return context
