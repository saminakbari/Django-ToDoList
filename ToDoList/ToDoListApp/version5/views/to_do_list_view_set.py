from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from ToDoListApp.models import ToDoList
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
        to_do_list = get_object_or_404(queryset, pk=pk)
        to_do_list.delete()
        return Response("To-do list deleted successfully.")
