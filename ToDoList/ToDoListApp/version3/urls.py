from django.urls import path

from ToDoListApp.version3.views import (
    AddSharedTasks,
    CreateList,
    CreateTask,
    DeleteList,
    DeleteTask,
    EditList,
    EditTask,
    GetList,
    GetTask,
    ShareTask,
    ShowLists,
)

v3_urlpatterns = [
    path("to-do-list/show-all/", ShowLists.as_view(), name="v3-show-lists"),
    path("to-do-list/create/", CreateList.as_view(), name="v3-create-list"),
    path("to-do-list/<int:list_id>/edit/", EditList.as_view(), name="v3-edit-list"),
    path(
        "to-do-list/<int:list_id>/delete/", DeleteList.as_view(), name="v3-delete-list"
    ),
    path("to-do-list/<int:list_id>/get/", GetList.as_view(), name="v3-get-list"),
    path(
        "to-do-list/<int:list_id>/task/create/",
        CreateTask.as_view(),
        name="v3-create-task",
    ),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/edit/",
        EditTask.as_view(),
        name="v3-edit-task",
    ),
    path("task/<int:task_id>/get/", GetTask.as_view(), name="v3-get-task"),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/delete/",
        DeleteTask.as_view(),
        name="v3-delete-task",
    ),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/share/",
        ShareTask.as_view(),
        name="v3-share-task",
    ),
    path(
        "to-do-list/<int:list_id>/task/shared-tasks/",
        AddSharedTasks.as_view(),
        name="v3-add-shared-tasks",
    ),
]
