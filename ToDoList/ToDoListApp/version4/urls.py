from django.urls import path

from ToDoListApp.version4.views.add_shared_task_view4 import AddSharedTask4
from ToDoListApp.version4.views.create_list_view4 import CreateList4
from ToDoListApp.version4.views.create_task_view4 import CreateTask4
from ToDoListApp.version4.views.delete_list_view4 import DeleteList4
from ToDoListApp.version4.views.delete_task_view4 import DeleteTask4
from ToDoListApp.version4.views.edit_list_view4 import EditList4
from ToDoListApp.version4.views.edit_task_view4 import EditTask4
from ToDoListApp.version4.views.get_list_view4 import GetList4
from ToDoListApp.version4.views.get_shared_tasks_view4 import GetSharedTasks4
from ToDoListApp.version4.views.get_task_view4 import GetTask4
from ToDoListApp.version4.views.share_task_view4 import ShareTask4
from ToDoListApp.version4.views.show_lists_view4 import ShowLists4

v4_urlpatterns = [
    path("to-do-list/show-all/", ShowLists4.as_view(), name='v4-show-lists'),
    path("to-do-list/create/", CreateList4.as_view(), name='v4-create-list'),
    path("to-do-list/<int:id>/edit/", EditList4.as_view(), name='v4-edit-list'),
    path("to-do-list/<int:id>/delete/", DeleteList4.as_view(), name='v4-delete-list'),
    path("to-do-list/<int:id>/get/", GetList4.as_view(), name='v4-get-list'),
    path("to-do-list/<int:id>/task/create/", CreateTask4.as_view(), name='v4-create-task'),
    path("task/<int:id>/edit/", EditTask4.as_view(), name='v4-edit-task'),
    path("task/<int:id>/get/", GetTask4.as_view(), name='v4-get-task'),
    path("to-do-list/<int:list_id>/task/<int:id>/delete/", DeleteTask4.as_view(), name='v4-delete-task'),
    path("task/<int:id>/share/", ShareTask4.as_view(), name='v4-share-task'),
    path("to-do-list/<int:id>/task/<int:task_id>/shared-tasks/", AddSharedTask4.as_view(), name='v4-add-shared-tasks'),
    path("task/get/not-added/", GetSharedTasks4.as_view(), name='v4-see-shared-tasks'),
]
