from django.contrib import admin

from ToDoListApp.models import ToDoList


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "all_tasks")
    list_filter = ("owner",)
    search_fields = ("title__startswith",)

    def all_tasks(self, obj):
        return "\n".join(
            [str(task.id) + ": " + task.title + " - " for task in obj.tasks.all()]
        )
