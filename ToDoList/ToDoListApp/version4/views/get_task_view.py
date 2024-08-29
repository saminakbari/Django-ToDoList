from rest_framework.generics import RetrieveAPIView

from ToDoListApp.serializers import TaskSerializer


class GetTaskView(RetrieveAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.request.user.all_tasks.all()
