from django.contrib import admin

from my_app.models import Task, ToDoList

admin.site.register(Task)
admin.site.register(ToDoList)
