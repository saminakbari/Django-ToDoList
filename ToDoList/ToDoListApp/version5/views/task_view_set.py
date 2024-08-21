from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class TaskViewSet(viewsets.ViewSet):
    def list(self, request, **kwargs):
        user_to_do_lists = request.user.to_do_lists.all()
        to_do_list = user_to_do_lists.get(pk=request.POST['list_id'])
        queryset = filter(lambda task: task in to_do_list.tasks.all(),
                          Task.objects.filter(owner=request.user))
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            user_to_do_lists = request.user.to_do_lists.all()
            to_do_list = user_to_do_lists.get(pk=request.POST['list_id'])
            task.to_do_lists.add(to_do_list)
            task.owner = request.user
            task.save()
            return Response("Task created successfully.")
        else:
            return Response("Invalid data.")

    def retrieve(self, request, task_id=None):
        queryset = Task.objects.filter(owner=request.user)
        task = get_object_or_404(queryset, pk=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def partial_update(self, request, task_id=None):
        queryset = Task.objects.filter(owner=request.user)
        task = get_object_or_404(queryset, pk=task_id)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Invalid data.")

    def destroy(self, request, task_id=None):
        queryset = Task.objects.filter(owner=request.user)
        task = get_object_or_404(queryset, pk=task_id)
        user_lists = request.user.to_do_lists
        to_do_list = user_lists.get(pk=request.POST['list_id'])
        to_do_list.tasks.remove(task)
        return Response("Task deleted successfully.")

    @action(detail=True, methods=['post'])
    def share_task(self, request, task_id=None):
        user_to_be_shared_with = User.objects.get(username=request.POST['username'])
        user_tasks = request.user.tasks
        task = user_tasks.get(id=task_id)
        user_to_be_shared_with.tasks_shared_with_user.add(task)
        result = "Task shared with " + user_to_be_shared_with.username + " successfully."
        return Response(result)

    @action(detail=True, method=['get'])
    def get_shared_tasks(self, request):
        serializer = TaskSerializer(request.user.tasks_shared_with_user.all(), many=True)
        return Response(serializer.data)
