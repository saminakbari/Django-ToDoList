from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import DestroyAPIView

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class DeleteList(LoginRequiredMixin, DestroyAPIView):
    serializer_class = ToDoListSerializer
    lookup_field = "id"

    def get_queryset(self):
        return ToDoList.objects.filter(owner=self.request.user)
