from rest_framework.generics import RetrieveUpdateDestroyAPIView

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class DeleteListView(RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        return ToDoList.objects.filter(owner=self.request.user)
