from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class TaskModelViewSet(LoginRequiredMixin, ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        if self.action == "list" or self.action == "destroy":
            to_do_list = self.get_list_by_id()
            return to_do_list.tasks.all()
        if self.action == "get_shared_tasks":
            return self.request.user.tasks_shared_with_user.all()
        if self.action in ["update", "partial_update"]:
            return Task.objects.all()
        return Task.objects.filter(owner=self.request.user)

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, *args, **kwargs):
        return super(TaskModelViewSet, self).list(request, *args, **kwargs)

    def perform_create(self, serializer):
        task = serializer.save()
        task.owner = self.request.user
        to_do_list = self.get_list_by_id()
        task.to_do_lists.add(to_do_list)
        return super(TaskModelViewSet, self).perform_create(serializer)

    def perform_destroy(self, instance):
        to_do_list = self.get_list_by_id()
        to_do_list.tasks.remove(instance)

    def perform_update(self, serializer):
        task = self.get_object()
        if task.owner != self.request.user:
            return Response("You don't own this task.")
        return super(TaskModelViewSet, self).perform_update(serializer)

    def partial_update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.owner != self.request.user:
            return Response("You don't own this task.")
        return super(TaskModelViewSet, self).partial_update(request, *args, **kwargs)

    @action(detail=True, methods=["post"])
    def share_task(self, request, *args, **kwargs):
        try:
            user_to_be_shared_with = User.objects.get(username=request.POST["username"])
        except User.DoesNotExist:
            return Response("There is no user with this id.")
        user_tasks = request.user.tasks
        try:
            task = user_tasks.get(pk=self.kwargs["pk"])
        except Task.DoesNotExist:
            return Response("You don't have a task with this id.")
        if task not in user_to_be_shared_with.tasks_shared_with_user.all():
            user_to_be_shared_with.tasks_shared_with_user.add(task)
            result = (
                    "Task shared with " + user_to_be_shared_with.username + " successfully."
            )
            return Response(result)
        else:
            return Response("You have already shared this task with this user.")

    @method_decorator(cache_page(60 * 60 * 2))
    @action(methods=["get"], detail=False)
    def get_shared_tasks(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @action(methods=["post"], detail=True)
    def add_shared_task(self, request, *args, **kwargs):
        try:
            task = Task.objects.all().get(pk=kwargs["pk"])
        except Task.DoesNotExist:
            return Response("Task with this id has not been shared with you.")
        to_do_list = request.user.to_do_lists.get(pk=request.POST["list_id"])
        if task in to_do_list.tasks.all():
            return Response("You already have this task in this list.")
        else:
            to_do_list.tasks.add(task)
            return Response("Task added successfully.")

    def get_list_by_id(self):
        user_lists = self.request.user.to_do_lists
        to_do_list = get_object_or_404(user_lists, pk=self.request.POST["list_id"])
        return to_do_list
