from rest_framework.generics import RetrieveAPIView

from ToDoListApp.serializers import TaskSerializer


class GetTaskView(RetrieveAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.request.user.shared_added_tasks.all() | self.request.user.tasks.all()
