from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
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

    def perform_create(self, serializer):
        serializer.context['user'] = self.request.user
        return super(ToDoListModelViewSet, self).perform_create(serializer)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.get_object(), data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return super(ToDoListModelViewSet, self).update(serializer)
        else:
            return Response(serializer.errors)
