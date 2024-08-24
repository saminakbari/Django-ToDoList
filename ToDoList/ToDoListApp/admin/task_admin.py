from django.contrib import admin

from ToDoListApp.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "deadline",
        "priority",
        "owner",
        "attachment",
        "all_lists",
    )

    def all_lists(self, obj):
        return [
            str(to_do_list.id) + ": " + to_do_list.title + " - "
            for to_do_list in obj.to_do_lists.all()
        ]
