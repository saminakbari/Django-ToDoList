from django.contrib import admin
from django.urls import path

from my_app.views.login_view import login_user
from my_app.views.register_login_view import register_or_login
from my_app.views.register_view import register_user
from my_app.views.create_list_view import create_list
from my_app.views.create_task_view import create_task
from my_app.views.delete_list_view import delete_list
from my_app.views.delete_task_view import delete_task
from my_app.views.edit_list_view import edit_to_do_list
from my_app.views.edit_task_view import edit_task
from my_app.views.get_list_view import get_list
from my_app.views.get_task_view import get_task
from my_app.views.share_task_view import share_task
from my_app.views.add_shared_tasks_view import show_shared_tasks
from my_app.views.show_all_lists_view import show_all_lists

urlpatterns = [
    path('admin/', admin.site.urls),
    path("to-do-list/showall/<str:username>/", show_all_lists),
    path("to-do-list/create/<str:username>/", create_list),
    path("to-do-list/edit/<int:list_id>/", edit_to_do_list),
    path("to-do-list/delete/<int:list_id>/", delete_list),
    path("to-do-list/get/<int:list_id>/", get_list),
    path("task/create/<int:list_id>/", create_task),
    path("task/edit/<int:task_id>/<str:username>/", edit_task),
    path("task/delete/<int:task_id>/<int:list_id>/", delete_task),
    path("task/get/<int:task_id>/", get_task),
    path("user/register/", register_user),
    path("user/login/", login_user),
    path("task/share/<int:task_id>/", share_task),
    path("task/shared-tasks/<str:username>/<int:list_id>/", show_shared_tasks),
    path("to-do-list/app/opening/", register_or_login),
]
