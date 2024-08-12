from django.contrib import admin

from my_app.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_id', 'title', 'description', 'deadline', 'priority', 'owner')
