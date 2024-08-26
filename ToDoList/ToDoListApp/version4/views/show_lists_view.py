from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import ListAPIView

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class ShowLists(LoginRequiredMixin, ListAPIView):
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        return ToDoList.objects.filter(owner=self.request.user)
