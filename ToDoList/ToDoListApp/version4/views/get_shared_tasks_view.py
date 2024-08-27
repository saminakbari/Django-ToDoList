from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from ToDoListApp.models import Task
from ToDoListApp.serializers import TaskSerializer


class GetSharedTasks(LoginRequiredMixin, ListAPIView):
    model = Task
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.tasks_shared_with_user.all()

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, *args, **kwargs):
        # print("get is called") --> for testing
        return super(GetSharedTasks, self).get(request, *args, **kwargs)
