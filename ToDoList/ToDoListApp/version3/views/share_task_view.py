from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView

from ToDoListApp.models import Task


class ShareTaskView(TemplateView):
    template_name = "v3/v3_share_task_template.html"

    def post(self, request, *args, **kwargs):
        task_id = kwargs["task_id"]
        task = Task.objects.get(pk=task_id)
        receiver_username = request.POST.get("receiver_username")
        try:
            receiver_user = User.objects.get(username=receiver_username)
        except User.DoesNotExist:
            messages.add_message(request, messages.INFO, "Username does not exist")
            return self.get(request, *args, **kwargs)

        receiver_user.tasks_shared_with_user.add(task)
        messages.add_message(request, messages.INFO, "Task is shared successfully.")
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["list_id"] = self.kwargs["list_id"]
        return context
