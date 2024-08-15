from django.contrib import admin

from ToDoListApp.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'deadline', 'priority', 'owner')
