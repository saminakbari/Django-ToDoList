from django.urls import path

from ToDoListApp.version4.views import (
    AddSharedTaskView,
    CreateListView,
    CreateTaskView,
    DeleteListView,
    DeleteTaskView,
    EditListView,
    EditTaskView,
    GetListView,
    GetSharedTasksView,
    GetTaskView,
    ShareTaskView,
    ShowListsView,
)

v4_urlpatterns = [
    path("to-do-list/show-all/", ShowListsView.as_view(), name="v4-show-lists"),
    path("to-do-list/create/", CreateListView.as_view(), name="v4-create-list"),
    path("to-do-list/<int:pk>/edit/", EditListView.as_view(), name="v4-edit-list"),
    path("to-do-list/<int:pk>/delete/", DeleteListView.as_view(), name="v4-delete-list"),
    path("to-do-list/<int:pk>/get/", GetListView.as_view(), name="v4-get-list"),
    path(
        "to-do-list/<int:pk>/task/create/", CreateTaskView.as_view(), name="v4-create-task"
    ),
    path("task/<int:pk>/edit/", EditTaskView.as_view(), name="v4-edit-task"),
    path("task/<int:pk>/get/", GetTaskView.as_view(), name="v4-get-task"),
    path(
        "to-do-list/<int:list_id>/task/<int:pk>/delete/",
        DeleteTaskView.as_view(),
        name="v4-delete-task",
    ),
    path("task/<int:pk>/share/", ShareTaskView.as_view(), name="v4-share-task"),
    path(
        "to-do-list/<int:pk>/add-shared-tasks/",
        AddSharedTaskView.as_view(),
        name="v4-add-shared-tasks",
    ),
    path("task/get/shared/", GetSharedTasksView.as_view(), name="v4-get-shared-tasks"),
]
