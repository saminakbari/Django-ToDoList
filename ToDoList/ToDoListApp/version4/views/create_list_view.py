from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import CreateAPIView

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class CreateListView(LoginRequiredMixin, CreateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer

    def perform_create(self, serializer):
        to_do_list = serializer.save()
        to_do_list.owner = self.request.user
        to_do_list.save()
        return super(CreateListView, self).perform_create(serializer)
