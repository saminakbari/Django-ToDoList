from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import CreateAPIView

from ToDoListApp.models import Task, ToDoList
from ToDoListApp.serializers import TaskSerializer


class CreateTaskView(LoginRequiredMixin, CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.context['user'] = self.request.user
        to_do_list = ToDoList.objects.get(pk=self.kwargs["pk"])
        serializer.context['to_do_list'] = to_do_list
        return super(CreateTaskView, self).perform_create(serializer)
