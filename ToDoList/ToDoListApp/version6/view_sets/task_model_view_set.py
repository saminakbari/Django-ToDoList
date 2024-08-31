from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class TaskModelViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        if self.action == "list" or self.action == "destroy":
            to_do_list = self.get_list_by_id()
            return to_do_list.tasks.all()
        if self.action == "get_shared_tasks":
            return self.request.user.tasks_shared_with_user.all()
        if self.action in ["update", "partial_update"]:
            return self.request.user.tasks.all()
        return Task.objects.filter(owner=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        context["to_do_list"] = self.get_list_by_id()

    @method_decorator(cache_page(60 * 30))
    def list(self, request, *args, **kwargs):
        return super(TaskModelViewSet, self).list(request, *args, **kwargs)

    def perform_destroy(self, instance):
        to_do_list = self.get_list_by_id()
        to_do_list.tasks.remove(instance)

    @action(detail=True, methods=["post"])
    def share_task(self, request, *args, **kwargs):
        try:
            user_to_be_shared_with = User.objects.get(username=request.POST["username"])
        except User.DoesNotExist:
            return Response("There is no user with this username.", status=404)
        user_tasks = request.user.tasks
        try:
            task = user_tasks.get(pk=self.kwargs["pk"])
        except Task.DoesNotExist:
            return Response("You don't own a task with this id.", status=404)
        if task not in user_to_be_shared_with.tasks_shared_with_user.all():
            user_to_be_shared_with.tasks_shared_with_user.add(task)
            result = (
                "Task shared with " + user_to_be_shared_with.username + " successfully."
            )
            return Response(result, status=200)
        else:
            return Response(
                "You have already shared this task with this user.", status=200
            )

    @method_decorator(cache_page(60 * 30))
    @action(methods=["get"], detail=False)
    def get_shared_tasks(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_list_by_id(self):
        user_lists = self.request.user.to_do_lists
        if self.request.POST['list_id']:
            to_do_list = get_object_or_404(user_lists, pk=self.request.POST["list_id"])
            return to_do_list
        return None
