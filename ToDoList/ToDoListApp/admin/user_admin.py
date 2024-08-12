from django.contrib import admin

from ToDoListApp.models import MyUser


@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
