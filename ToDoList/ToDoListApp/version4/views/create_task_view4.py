from rest_framework import generics
from rest_framework.response import Response

from ToDoListApp.models import Task, ToDoList
from ToDoListApp.serializers import TaskSerializer


class CreateTask4(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        to_do_list = ToDoList.objects.get(pk=self.kwargs['list_id'])
        task.to_do_lists.add(to_do_list)
        task.owner = self.request.user
        task.save()
        return super(CreateTask4, self).perform_create(serializer)
