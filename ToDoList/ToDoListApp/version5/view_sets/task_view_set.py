from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ToDoListApp.models import Task, ToDoList
from ToDoListApp.serializers import TaskSerializer


class TaskViewSet(ViewSet):
    @method_decorator(cache_page(60 * 30))
    def list(self, request, **kwargs):
        user_to_do_lists = request.user.to_do_lists.all()
        try:
            to_do_list = user_to_do_lists.get(pk=request.POST["list_id"])
        except ToDoList.DoesNotExist:
            return Response("You don't have a to-do list with this id.", status=404)
        queryset = filter(
            lambda task: task in to_do_list.tasks.all(),
            Task.objects.filter(owner=request.user),
        )
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def create(self, request, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            user_to_do_lists = request.user.to_do_lists.all()
            try:
                to_do_list = user_to_do_lists.get(pk=request.POST["list_id"])
            except ToDoList.DoesNotExist:
                return Response("You don't have a to-do list with this id.", status=404)
            task.to_do_lists.add(to_do_list)
            task.owner = request.user
            task.save()
            return Response("Task created successfully.", status=201)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, task_id=None):
        queryset = Task.objects.filter(owner=request.user)
        try:
            task = queryset.get(pk=task_id)
        except Task.DoesNotExist:
            return Response("You don't have a task with this id.", status=404)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=400)

    def partial_update(self, request, pk=None):
        queryset = Task.objects.filter(owner=request.user)
        user_lists = request.user.to_do_lists.all()
        try:
            task = queryset.get(pk=pk)
        except Task.DoesNotExist:
            if any(lambda: task in to_do_list.tasks for to_do_list in user_lists):
                return Response("You don't have access to edit this task.", status=400)
            return Response("You don't have a task with this id.", status=404)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Task updated successfully.", status=200)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = Task.objects.filter(owner=request.user)
        try:
            task = queryset.get(pk=pk)
        except Task.DoesNotExist:
            user_lists = request.user.to_do_lists.all()
            if any(lambda: task in to_do_list.tasks for to_do_list in user_lists):
                return Response("You don't have access to edit this task.", status=403)
            return Response("You don't have a task with this id.", status=404)
        user_lists = request.user.to_do_lists
        try:
            to_do_list = user_lists.get(pk=request.POST["list_id"])
        except ToDoList.DoesNotExist:
            return Response("You don't have a list with this id.", status=404)
        if task in to_do_list.tasks.all():
            to_do_list.tasks.remove(task)
            return Response("Task deleted successfully.", status=200)
        else:
            return Response("There is no task with this id in this list.", status=404)

    @action(detail=True, methods=["post"])
    def share_task(self, request, task_id=None):
        try:
            user_to_be_shared_with = User.objects.get(username=request.POST["username"])
        except User.DoesNotExist:
            return Response("There is no user with this id.", status=404)
        user_tasks = request.user.tasks
        try:
            task = user_tasks.get(id=task_id)
        except Task.DoesNotExist:
            return Response("You don't have a task with this id.", status=404)
        if task not in user_to_be_shared_with.tasks_shared_with_user.all():
            user_to_be_shared_with.tasks_shared_with_user.add(task)
            result = (
                "Task shared with " + user_to_be_shared_with.username + " successfully."
            )
            return Response(result, status=200)
        else:
            return Response(
                "You have already shared this task with this user.", status=400
            )

    @action(detail=True, methods=["get"])
    def get_shared_tasks(self, request):
        serializer = TaskSerializer(
            request.user.tasks_shared_with_user.all(), many=True
        )
        return Response(serializer.data, status=200)
