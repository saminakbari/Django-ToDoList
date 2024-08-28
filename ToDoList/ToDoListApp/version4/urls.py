from django.urls import path

from ToDoListApp.version4.views import (
    AddSharedTask,
    CreateList,
    CreateTask,
    DeleteList,
    DeleteTask,
    EditList,
    EditTask,
    GetList,
    GetSharedTasks,
    GetTask,
    ShareTask,
    ShowLists,
)

v4_urlpatterns = [
    path("to-do-list/show-all/", ShowLists.as_view(), name="v4-show-lists"),
    path("to-do-list/create/", CreateList.as_view(), name="v4-create-list"),
    path("to-do-list/<int:pk>/edit/", EditList.as_view(), name="v4-edit-list"),
    path("to-do-list/<int:pk>/delete/", DeleteList.as_view(), name="v4-delete-list"),
    path("to-do-list/<int:pk>/get/", GetList.as_view(), name="v4-get-list"),
    path(
        "to-do-list/<int:pk>/task/create/", CreateTask.as_view(), name="v4-create-task"
    ),
    path("task/<int:pk>/edit/", EditTask.as_view(), name="v4-edit-task"),
    path("task/<int:pk>/get/", GetTask.as_view(), name="v4-get-task"),
    path(
        "to-do-list/<int:list_id>/task/<int:pk>/delete/",
        DeleteTask.as_view(),
        name="v4-delete-task",
    ),
    path("task/<int:pk>/share/", ShareTask.as_view(), name="v4-share-task"),
    path(
        "to-do-list/<int:pk>/add-shared-tasks/",
        AddSharedTask.as_view(),
        name="v4-add-shared-tasks",
    ),
    path("task/get/shared/", GetSharedTasks.as_view(), name="v4-get-shared-tasks"),
]
