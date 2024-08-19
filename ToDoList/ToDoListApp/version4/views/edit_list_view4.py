from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.response import Response

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class EditList4(LoginRequiredMixin, generics.UpdateAPIView):
    serializer_class = ToDoListSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return ToDoList.objects.filter(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response("To-do list edited successfully.")

        else:
            return Response({"message": "failed", "details": serializer.errors})

