from django.contrib import admin
from django.urls import path

from my_app.views.create_list_view import create_list
from my_app.views.create_task_view import create_task
from my_app.views.delete_list_view import delete_list
from my_app.views.delete_task_view import delete_task
from my_app.views.edit_list_view import edit_to_do_list
from my_app.views.edit_task_view import edit_task
from my_app.views.get_list_view import get_list
from my_app.views.get_task_view import get_task
from my_app.views.show_all_lists_view import show_all_lists

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("to-do-list/create/<str:title>/", create_list),
    path("to-do-list/getall/", show_all_lists),
    path("to-do-list/create/", create_list),
    path("to-do-list/edit/<int:list_id>/", edit_to_do_list),
    path("to-do-list/delete/<int:list_id>/", delete_list),
    path("to-do-list/get/<int:list_id>/", get_list),
    path("task/create/", create_task),
    # path("task/create/<str:title>/<str:description>/<str:priority>/<int:list_id>/", create_task),
    path("task/edit/<int:task_id>/", edit_task),
    path("task/delete/<int:task_id>/", delete_task),
    path("task/get/<int:task_id>/", get_task),
    # path("user/register/", register_user),
    # path("user/login/", login_user),
]
