from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class TaskModelViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.owner)

    def perform_create(self, serializer):
        task = serializer.save()
        task.owner = self.request.user
        user_lists = self.request.user.to_do_lists
        to_do_list = user_lists.get(pk=self.request.POST['list_id'])
        task.to_do_lists.add(to_do_list)
        return super(TaskModelViewSet, self).perform_create(serializer)

    
