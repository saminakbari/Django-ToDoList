from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from rest_framework.response import Response

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class ToDoListModelViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        return ToDoList.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        to_do_list = serializer.save()
        to_do_list.owner = self.request.user
        to_do_list.save()
        return super(ToDoListModelViewSet, self).perform_create(serializer)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(),
                                           data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return super(ToDoListModelViewSet, self).update(serializer)
        else:
            return Response(serializer.errors)

    
