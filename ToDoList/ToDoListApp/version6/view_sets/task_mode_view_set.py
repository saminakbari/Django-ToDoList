from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from ToDoListApp.models import Task, ToDoList
from ToDoListApp.serializers import TaskSerializer


class TaskModelViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        if self.action == 'list':
            user_lists = self.request.user.to_do_lists
            to_do_list = get_object_or_404(user_lists, pk=self.request.POST['list_id'])
            return to_do_list.tasks.all()
        return Task.objects.filter(owner=self.request.owner)

    def perform_create(self, serializer):
        task = serializer.save()
        task.owner = self.request.user
        user_lists = self.request.user.to_do_lists
        to_do_list = user_lists.get(pk=self.request.POST['list_id'])
        task.to_do_lists.add(to_do_list)
        return super(TaskModelViewSet, self).perform_create(serializer)


