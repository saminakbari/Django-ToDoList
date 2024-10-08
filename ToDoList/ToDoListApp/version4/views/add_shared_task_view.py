from rest_framework.response import Response
from rest_framework.views import APIView

from ToDoListApp.models import Task, ToDoList


class AddSharedTaskView(APIView):
    def post(self, request, **kwargs):
        task_id = self.request.data["task_id"]
        task = Task.objects.get(pk=task_id)
        to_do_list = ToDoList.objects.get(pk=self.kwargs["pk"])
        to_do_list.tasks.add(task)
        task.users_who_can_see.add(request.user)
        request.user.shared_added_tasks.add(task)
        return Response("Task added successfully.", status=200)
