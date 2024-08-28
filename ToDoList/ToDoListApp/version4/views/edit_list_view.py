from rest_framework.generics import UpdateAPIView

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class EditListView(UpdateAPIView):
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        return ToDoList.objects.filter(owner=self.request.user)
