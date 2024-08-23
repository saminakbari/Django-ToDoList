from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ToDoListApp.models import Task, ToDoList
from ToDoListApp.serializers import TaskSerializer


class TaskModelViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        if self.action == 'list' or self.action == 'destroy':
            user_lists = self.request.user.to_do_lists
            to_do_list = get_object_or_404(user_lists, pk=self.request.POST['list_id'])
            return to_do_list.tasks.all()
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        task = serializer.save()
        task.owner = self.request.user
        to_do_list = self.get_list_by_id()
        task.to_do_lists.add(to_do_list)
        return super(TaskModelViewSet, self).perform_create(serializer)

    def perform_destroy(self, instance):
        to_do_list = self.get_list_by_id()
        to_do_list.tasks.remove(instance)

    @action(detail=True, methods=['post'])
    def share_task(self, request, *args, **kwargs):
        try:
            user_to_be_shared_with = User.objects.get(username=request.POST['username'])
        except User.DoesNotExist:
            return Response("There is no user with this id.")
        user_tasks = request.user.tasks
        try:
            task = user_tasks.get(pk=self.kwargs['pk'])
        except Task.DoesNotExist:
            return Response("You don't have a task with this id.")
        if task not in user_to_be_shared_with.tasks_shared_with_user.all():
            user_to_be_shared_with.tasks_shared_with_user.add(task)
            result = ("Task shared with " + user_to_be_shared_with.username
                      + " successfully.")
            return Response(result)
        else:
            return Response("You have already shared this task with this user.")

    def get_list_by_id(self):
        user_lists = self.request.user.to_do_lists
        to_do_list = user_lists.get(pk=self.request.POST['list_id'])
        return to_do_list
