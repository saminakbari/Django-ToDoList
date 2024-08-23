from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ToDoListApp.models import Task, ToDoList
from ToDoListApp.serializers import TaskSerializer


class TaskViewSet(LoginRequiredMixin, viewsets.ViewSet):
    def list(self, request, **kwargs):
        user_to_do_lists = request.user.to_do_lists.all()
        try:
            to_do_list = user_to_do_lists.get(pk=request.POST['list_id'])
        except ToDoList.DoesNotExist:
            return Response("You don't have a to-do list with this id.")
        queryset = filter(lambda task: task in to_do_list.tasks.all(),
                          Task.objects.filter(owner=request.user))
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            user_to_do_lists = request.user.to_do_lists.all()
            try:
                to_do_list = user_to_do_lists.get(pk=request.POST['list_id'])
            except ToDoList.DoesNotExist:
                return Response("You don't have a to-do list with this id.")
            task.to_do_lists.add(to_do_list)
            task.owner = request.user
            task.save()
            return Response("Task created successfully.")
        else:
            return Response(serializer.errors)

    def retrieve(self, request, task_id=None):
        queryset = Task.objects.filter(owner=request.user)
        try:
            task = queryset.get(pk=task_id)
        except:
            return Response("You don't have a task with this id.")
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = Task.objects.filter(owner=request.user)
        user_lists = request.user.to_do_lists.all()
        try:
            task = queryset.get(pk=pk)
        except Task.DoesNotExist:
            if any(lambda: task in to_do_list.tasks for to_do_list in user_lists):
                return Response("You don't have access to edit this task.")
            return Response("You don't have a task with this id.")
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Task updated successfully.")
        else:
            return Response(serializer.errors)

    def destroy(self, request, pk=None):
        queryset = Task.objects.filter(owner=request.user)
        try:
            task = queryset.get(pk=pk)
        except Task.DoesNotExist:
            user_lists = request.user.to_do_lists.all()
            if any(lambda: task in to_do_list.tasks for to_do_list in user_lists):
                return Response("You don't have access to edit this task.")
            return Response("You don't have a task with this id.")
        user_lists = request.user.to_do_lists
        try:
            to_do_list = user_lists.get(pk=request.POST['list_id'])
        except ToDoList.DoesNotExist:
            return Response("You don't have a list with this id.")
        if task in to_do_list.tasks.all():
            to_do_list.tasks.remove(task)
            return Response("Task deleted successfully.")
        else:
            return Response("There is no task with this id in the list.")

    @action(detail=True, methods=['post'])
    def share_task(self, request, task_id=None):
        try:
            user_to_be_shared_with = User.objects.get(username=request.POST['username'])
        except User.DoesNotExist:
            return "There is no user with this id."
        user_tasks = request.user.tasks
        try:
            task = user_tasks.get(id=task_id)
        except Task.DoesNotExist:
            return "You don't have a task with this id."
        if task not in user_to_be_shared_with.tasks_shared_with_user.all():
            user_to_be_shared_with.tasks_shared_with_user.add(task)
            result = ("Task shared with " + user_to_be_shared_with.username
                      + " successfully.")
            return Response(result)
        else:
            return Response("You have already shared this task with this user.")

    @action(detail=True, methods=['get'])
    def get_shared_tasks(self, request):
        serializer = TaskSerializer(request.user.tasks_shared_with_user.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_shared_task(self, request, pk=None):
        try:
            task = Task.objects.all().get(pk=pk)
        except Task.DoesNotExist:
            return Response("Task with this id has not been shared with you.")
        to_do_list = request.user.to_do_lists.get(pk=request.POST['list_id'])
        if task in to_do_list.tasks.all():
            return Response("You already have this task in this list.")
        else:
            to_do_list.tasks.add(task)
            return Response("Task added successfully.")
