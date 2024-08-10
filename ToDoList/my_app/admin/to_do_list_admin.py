from django.contrib import admin

from my_app.models import ToDoList


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('list_id', 'title')


# admin.site.register(ToDoList, ToDoListAdmin)
