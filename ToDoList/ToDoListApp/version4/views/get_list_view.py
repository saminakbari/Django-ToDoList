from rest_framework.generics import RetrieveAPIView

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class GetListView(RetrieveAPIView):
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        return ToDoList.objects.filter(owner=self.request.user)
