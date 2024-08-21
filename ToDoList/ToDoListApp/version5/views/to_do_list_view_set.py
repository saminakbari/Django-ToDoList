from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ToDoListApp.models import ToDoList, Task
from ToDoListApp.serializers import ToDoListSerializer


class ToDoListViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = ToDoList.objects.filter(owner=request.user)
        serializer = ToDoListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ToDoListSerializer(data=request.data)
        if serializer.is_valid():
            to_do_list = serializer.save()
            to_do_list.owner = request.user
            to_do_list.save()
            print(to_do_list.title)
            return Response("To-do list added successfully.")
        else:
            return Response("Invalid data")

    def retrieve(self, request, pk=None):
        queryset = ToDoList.objects.filter(owner=request.user)
        to_do_list = get_object_or_404(queryset, pk=pk)
        serializer = ToDoListSerializer(to_do_list)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = ToDoList.objects.filter(owner=request.user)
        to_do_list = get_object_or_404(queryset, pk=pk)
        serializer = ToDoListSerializer(to_do_list, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Invalid data")

    def destroy(self, request, pk=None):
        queryset = ToDoList.objects.filter(owner=request.user)
        try:
            to_do_list = get_object_or_404(queryset, pk=pk)
        except ToDoList.DoesNotExist:
            return Response("You don't have a to-do list with this id.")
        to_do_list.delete()
        return Response("To-do list deleted successfully.")

    @action(detail=True, methods=['post'])
    def add_shared_task(self, request, pk=None):
        try:
            task = Task.objects.all().get(pk=request.POST['task_id'])
        except Task.DoesNotExist:
            return Response("Task with this id has not been shared with you.")
        to_do_list = request.user.to_do_lists.get(pk=pk)
        if task in to_do_list.tasks.all():
            return Response("You already have this task in this list.")
        else:
            to_do_list.tasks.add(task)
            return Response("Task added successfully.")
