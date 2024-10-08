from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ToDoListApp.models import Task, ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class ToDoListViewSet(ViewSet):
    @method_decorator(cache_page(60 * 30))
    def list(self, request):
        queryset = ToDoList.objects.filter(owner=request.user)
        serializer = ToDoListSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def create(self, request):
        serializer = ToDoListSerializer(data=request.data)
        serializer.context["user"] = request.user
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
            return Response("You don't have a list with this id.", status=404)
        serializer = ToDoListSerializer(to_do_list)
        return Response(serializer.data, status=200)

    def partial_update(self, request, pk=None):
        queryset = ToDoList.objects.filter(owner=request.user)
        try:
            to_do_list = queryset.get(pk=pk)
        except ToDoList.DoesNotExist:
            return Response("You don't have a list with this id.", status=404)
        serializer = ToDoListSerializer(to_do_list, data=request.data, partial=True)
        serializer.context["user"] = request.user
        if serializer.is_valid():
            serializer.save()
            return Response("To-do list updated successfully.", status=200)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = ToDoList.objects.filter(owner=request.user)
        try:
            to_do_list = queryset.get(pk=pk)
        except ToDoList.DoesNotExist:
            return Response("You don't have a to-do list with this id.", status=404)
        to_do_list.delete()
        return Response("To-do list deleted successfully.", status=200)

    @action(detail=True, methods=["post"])
    def add_shared_task(self, request, pk=None):
        try:
            task = Task.objects.all().get(pk=request.POST["task_id"])
        except Task.DoesNotExist:
            return Response(
                "Task with this id has not been shared with you.", status=404
            )
        to_do_list = request.user.to_do_lists.get(pk=pk)
        if task in to_do_list.tasks.all():
            return Response("You already have this task in this list.", status=400)
        else:
            to_do_list.tasks.add(task)
            task.users_who_can_see.add(request.user)
            return Response("Task added successfully.", status=200)
