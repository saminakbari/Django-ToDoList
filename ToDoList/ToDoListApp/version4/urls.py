from django.urls import path

from ToDoListApp.version4.views.create_list_view4 import CreateList4
from ToDoListApp.version4.views.create_task_view4 import CreateTask4
from ToDoListApp.version4.views.delete_list_view4 import DeleteList4
from ToDoListApp.version4.views.edit_list_view4 import EditList4
from ToDoListApp.version4.views.show_lists_view4 import ShowLists4

v4_urlpatterns = [
    path("to-do-list/show-all/", ShowLists4.as_view(), name='v4-show-lists'),
    path("to-do-list/create/", CreateList4.as_view(), name='v4-create-list'),
    path("to-do-list/<int:id>/edit/", EditList4.as_view(), name='v4-edit-list'),
    path("to-do-list/<int:id>/delete/", DeleteList4.as_view(), name='v4-delete-list'),
    # path("to-do-list/<int:list_id>/get/", GetList4.as_view(), name='v4-get-list'),
    path("to-do-list/<int:list_id>/task/create/", CreateTask4.as_view(), name='v4-create-task'),
    # path("to-do-list/<int:list_id>/task/<int:task_id>/edit/", EditTask4.as_view(), name='v4-edit-task'),
    # path("task/<int:task_id>/get/", GetTask4.as_view(), name='v4-get-task'),
    # path("to-do-list/<int:list_id>/task/<int:task_id>/delete/", DeleteTask4.as_view(), name='v4-delete-task'),
    # path("to-do-list/<int:list_id>/task/<int:task_id>/share/", ShareTask4.as_view(), name='v4-share-task'),
    # path("to-do-list/<int:list_id>/task/shared-tasks/", AddSharedTasks4.as_view(), name='v4-add-shared-tasks'),
]
