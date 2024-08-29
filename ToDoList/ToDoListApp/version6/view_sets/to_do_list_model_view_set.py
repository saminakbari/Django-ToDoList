from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from ToDoListApp.models import Task, ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class ToDoListModelViewSet(ModelViewSet):
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        return ToDoList.objects.filter(owner=self.request.user)

    @method_decorator(cache_page(60 * 30))
    def list(self, request, *args, **kwargs):
        return super(ToDoListModelViewSet, self).list(request, *args, **kwargs)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context

    @action(methods=["post"], detail=True)
    def add_shared_task(self, request, *args, **kwargs):
        try:
            task = Task.objects.all().get(pk=kwargs["pk"])
        except Task.DoesNotExist:
            return Response(
                "Task with this id has not been shared with you.", status=404
            )
        to_do_list = request.user.to_do_lists.get(pk=request.POST["list_id"])
        if task in to_do_list.tasks.all():
            return Response("You already have this task in this list.", status=200)
        else:
            to_do_list.tasks.add(task)
            return Response("Task added successfully.", status=200)
