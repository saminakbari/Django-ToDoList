from django.urls import path

from ToDoListApp.views import get_task
from ToDoListApp.views.add_shared_tasks_view import add_shared_tasks
from ToDoListApp.views.create_list_view import create_list
from ToDoListApp.views.create_task_view import create_task
from ToDoListApp.views.delete_list_view import delete_list
from ToDoListApp.views.delete_task_view import delete_task
from ToDoListApp.views.edit_list_view import edit_list
from ToDoListApp.views.edit_task_view import edit_task
from ToDoListApp.views.get_list_view import get_list
from ToDoListApp.views.share_task_view import share_task
from ToDoListApp.views.show_all_lists_view import show_all_lists

v1_urlpatterns = [
    path("to-do-list/showall/", show_all_lists, name='v1-show-lists'),
    path("to-do-list/create/", create_list, name='v1-create-list'),
    path("to-do-list/<int:list_id>/edit/", edit_list, name='v1-edit-list'),
    path("to-do-list/<int:list_id>/delete/", delete_list, name='v1-delete-list'),
    path("to-do-list/<int:list_id>/get/", get_list, name='v1-get-list'),
    path("to-do-list/<int:list_id>/task/create/", create_task, name='v1-create-task'),
    path("to-do-list/<int:list_id>/task/<int:task_id>/edit/", edit_task, name='v1-edit-task'),
    path("to-do-list/<int:list_id>/task/<int:task_id>/delete/", delete_task, name='v1-delete-task'),
    path("task/<int:task_id>/get/", get_task, name='v1-get-task'),
    path("task/<int:task_id>/share/", share_task, name='v1-share-task'),
    path("to-do-list/<int:list_id>/shared-tasks/", add_shared_tasks, name='v1-add-shared-tasks'),
]
