from django.contrib import admin

from my_app.models import Task, ToDoList

from my_app.models import Task, ToDoList, MyUser

admin.site.register(Task)
admin.site.register(ToDoList)
admin.site.register(MyUser)
