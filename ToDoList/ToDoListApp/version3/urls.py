from django.urls import path

from ToDoListApp.version3.views import (
    AddSharedTasksView,
    CreateListView,
    CreateTaskView,
    DeleteListView,
    DeleteTaskView,
    EditListView,
    EditTaskView,
    GetListView,
    GetTaskView,
    ShareTaskView,
    ShowListsView,
)

v3_urlpatterns = [
    path("to-do-list/show-all/", ShowListsView.as_view(), name="v3-show-lists"),
    path("to-do-list/create/", CreateListView.as_view(), name="v3-create-list"),
    path("to-do-list/<int:list_id>/edit/", EditListView.as_view(), name="v3-edit-list"),
    path(
        "to-do-list/<int:list_id>/delete/",
        DeleteListView.as_view(),
        name="v3-delete-list",
    ),
    path("to-do-list/<int:list_id>/get/", GetListView.as_view(), name="v3-get-list"),
    path(
        "to-do-list/<int:list_id>/task/create/",
        CreateTaskView.as_view(),
        name="v3-create-task",
    ),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/edit/",
        EditTaskView.as_view(),
        name="v3-edit-task",
    ),
    path("task/<int:task_id>/get/", GetTaskView.as_view(), name="v3-get-task"),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/delete/",
        DeleteTaskView.as_view(),
        name="v3-delete-task",
    ),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/share/",
        ShareTaskView.as_view(),
        name="v3-share-task",
    ),
    path(
        "to-do-list/<int:list_id>/task/shared-tasks/",
        AddSharedTasksView.as_view(),
        name="v3-add-shared-tasks",
    ),
]
