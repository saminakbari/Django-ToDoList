from rest_framework.generics import DestroyAPIView

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class DeleteListView(DestroyAPIView):
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        return ToDoList.objects.filter(owner=self.request.user)
