from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class ShowLists(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        return ToDoList.objects.filter(owner=self.request.user)
