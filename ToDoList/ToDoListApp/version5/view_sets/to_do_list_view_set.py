from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class ToDoListViewSet(LoginRequiredMixin, ViewSet):

    @method_decorator(cache_page(60 * 30))
    def list(self, request):
        queryset = ToDoList.objects.filter(owner=request.user)
        serializer = ToDoListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ToDoListSerializer(data=request.data)
        serializer.context['user'] = request.user
        if serializer.is_valid():
            serializer.save()
            return Response("To-do list created successfully.", status=201)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = ToDoList.objects.filter(owner=request.user)
        try:
            to_do_list = queryset.get(pk=pk)
        except ToDoList.DoesNotExist:
            return Response("You don't have a list with this id.")
        serializer = ToDoListSerializer(to_do_list)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = ToDoList.objects.filter(owner=request.user)
        try:
            to_do_list = queryset.get(pk=pk)
        except ToDoList.DoesNotExist:
            return Response("You don't have a list with this id.")
        serializer = ToDoListSerializer(to_do_list, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("To-do list updated successfully.")
        else:
            return Response(serializer.errors)

    def destroy(self, request, pk=None):
        queryset = ToDoList.objects.filter(owner=request.user)
        try:
            to_do_list = queryset.get(pk=pk)
        except ToDoList.DoesNotExist:
            return Response("You don't have a to-do list with this id.")
        to_do_list.delete()
        return Response("To-do list deleted successfully.")
