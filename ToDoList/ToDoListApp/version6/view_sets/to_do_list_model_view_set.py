from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ModelViewSet

from ToDoListApp.models import ToDoList
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
        context['user'] = self.request.user
        return context
