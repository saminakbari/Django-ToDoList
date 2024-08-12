from django.contrib import admin

from my_app.models import MyUser


@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
