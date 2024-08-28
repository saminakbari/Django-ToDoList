from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from ToDoListApp.models import ToDoList
from ToDoListApp.serializers import ToDoListSerializer


class GetListView(RetrieveAPIView):
    serializer_class = ToDoListSerializer

    def get_queryset(self):
        return ToDoList.objects.filter(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        to_do_list = self.get_object()
        result = {"title:": to_do_list.title}
        tasks = ""
        for task in to_do_list.tasks.all():
            tasks += task.title + " - "
        result["tasks"] = tasks
        return Response(result)
