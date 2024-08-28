from rest_framework.generics import CreateAPIView

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class CreateListView(CreateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer

    def get_serializer_context(self):
        context = super(CreateListView, self).get_serializer_context()
        context['user'] = self.request.user
        return context
