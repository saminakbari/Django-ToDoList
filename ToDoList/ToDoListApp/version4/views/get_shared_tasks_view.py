from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView

from ToDoListApp.serializers import TaskSerializer


class GetSharedTasksView(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.request.user.tasks_shared_with_user.all()

    @method_decorator(cache_page(60 * 30))
    def get(self, request, *args, **kwargs):
        # print("get is called") --> for testing
        return super(GetSharedTasksView, self).get(request, *args, **kwargs)
