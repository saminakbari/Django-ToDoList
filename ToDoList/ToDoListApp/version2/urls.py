from django.urls import path

from .views.add_shared_tasks_view2 import AddSharedTasks
from .views.create_list_view2 import CreateList
from .views.create_task_view2 import CreateTask
from .views.delete_list_view2 import DeleteList
from .views.delete_task_view2 import DeleteTask
from .views.edit_list_view2 import EditList
from .views.edit_task_view2 import EditTask
from .views.get_list_view2 import GetList
from .views.get_task_view2 import GetTask
from .views.share_task_view2 import ShareTask
from .views.show_lists_view2 import ShowLists

v2_urlpatterns = [
    path("to-do-list/show-all/", ShowLists.as_view(), name="v2-show-lists"),
    path("to-do-list/create/", CreateList.as_view(), name="v2-create-list"),
    path("to-do-list/<int:list_id>/edit/", EditList.as_view(), name="v2-edit-list"),
    path(
        "to-do-list/<int:list_id>/delete/", DeleteList.as_view(), name="v2-delete-list"
    ),
    path("to-do-list/<int:list_id>/get/", GetList.as_view(), name="v2-get-list"),
    path(
        "to-do-list/<int:list_id>/task/create/",
        CreateTask.as_view(),
        name="v2-create-task",
    ),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/edit/",
        EditTask.as_view(),
        name="v2-edit-task",
    ),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/delete/",
        DeleteTask.as_view(),
        name="v2-delete-task",
    ),
    path("task/<int:task_id>/get/", GetTask.as_view(), name="v2-get-task"),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/share/",
        ShareTask.as_view(),
        name="v2-share-task",
    ),
    path(
        "to-do-list/<int:list_id>/task/shared-tasks/",
        AddSharedTasks.as_view(),
        name="v2-add-shared-tasks",
    ),
]
