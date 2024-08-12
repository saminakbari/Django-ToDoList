from django.contrib import admin

from ToDoListApp.models import ToDoList


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('list_id', 'title')
