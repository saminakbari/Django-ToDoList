from django.contrib import admin

from ToDoListApp.models import Task2


@admin.register(Task2)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'deadline', 'priority', 'owner')
