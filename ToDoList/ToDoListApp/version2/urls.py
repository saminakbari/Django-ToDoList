from django.urls import path

from .views.add_shared_tasks_view import AddSharedTasksView
from .views.create_list_view import CreateListView
from .views.create_task_view import CreateTaskView
from .views.delete_list_view import DeleteListView
from .views.delete_task_view import DeleteTaskView
from .views.edit_list_view import EditListView
from .views.edit_task_view import EditTaskView
from .views.get_list_view import GetListView
from .views.get_task_view import GetTaskView
from .views.share_task_view import ShareTaskView
from .views.show_lists_view import ShowListsView

v2_urlpatterns = [
    path("to-do-list/show-all/", ShowListsView.as_view(), name="v2-show-lists"),
    path("to-do-list/create/", CreateListView.as_view(), name="v2-create-list"),
    path("to-do-list/<int:list_id>/edit/", EditListView.as_view(), name="v2-edit-list"),
    path(
        "to-do-list/<int:list_id>/delete/",
        DeleteListView.as_view(),
        name="v2-delete-list",
    ),
    path("to-do-list/<int:list_id>/get/", GetListView.as_view(), name="v2-get-list"),
    path(
        "to-do-list/<int:list_id>/task/create/",
        CreateTaskView.as_view(),
        name="v2-create-task",
    ),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/edit/",
        EditTaskView.as_view(),
        name="v2-edit-task",
    ),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/delete/",
        DeleteTaskView.as_view(),
        name="v2-delete-task",
    ),
    path("task/<int:task_id>/get/", GetTaskView.as_view(), name="v2-get-task"),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/share/",
        ShareTaskView.as_view(),
        name="v2-share-task",
    ),
    path(
        "to-do-list/<int:list_id>/task/shared-tasks/",
        AddSharedTasksView.as_view(),
        name="v2-add-shared-tasks",
    ),
]
