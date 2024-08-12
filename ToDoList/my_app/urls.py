from django.urls import path

from my_app.views import get_task
from my_app.views.add_shared_tasks_view import add_shared_tasks
from my_app.views.create_list_view import create_list
from my_app.views.create_task_view import create_task
from my_app.views.delete_list_view import delete_list
from my_app.views.delete_task_view import delete_task
from my_app.views.edit_list_view import edit_to_do_list
from my_app.views.edit_task_view import edit_task
from my_app.views.get_list_view import get_list
from my_app.views.share_task_view import share_task
from my_app.views.show_all_lists_view import show_all_lists

v1_urlpatterns = [
    path("to-do-list/showall/", show_all_lists),
    path("to-do-list/create/", create_list),
    path("to-do-list/edit/<int:list_id>/", edit_to_do_list),
    path("to-do-list/delete/<int:list_id>/", delete_list),
    path("to-do-list/get/<int:list_id>/", get_list),
    path("task/create/<int:list_id>/", create_task),
    path("task/edit/<int:task_id>/<int:list_id>/", edit_task),
    path("task/delete/<int:task_id>/<int:list_id>/", delete_task),
    path("task/get/<int:task_id>/", get_task),
    path("task/share/<int:task_id>/", share_task),
    path("task/shared-tasks/<int:list_id>/", add_shared_tasks),
]
