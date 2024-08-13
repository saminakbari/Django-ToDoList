from django.contrib import admin

from ToDoListApp.models import ToDoList2


@admin.register(ToDoList2)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
