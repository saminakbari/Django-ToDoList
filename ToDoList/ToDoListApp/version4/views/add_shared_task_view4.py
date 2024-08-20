from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class AddSharedTask4(LoginRequiredMixin, generics.RetrieveUpdateAPIView):
    pass
    # serializer_class = ToDoListSerializer
    # lookup_field = 'id'
    #
    # def get_queryset(self):
    #     return ToDoList.objects.filter(owner=self.request.user)
    #
    # def perform_update(self, serializer):
    #     task_id = self.request.data['task_id']
