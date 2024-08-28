from django.urls import path

from ToDoListApp.version4_1.views import (
    AddSharedTaskView,
    CreateListView,
    CreateTaskView,
    GetEditDeleteListView,
    GetEditDeleteTaskView,
    GetSharedTasksView,
    ShareTaskView,
    ShowListsView,
)

v4_1_urlpatterns = [
    path("to-do-list/show-all/", ShowListsView.as_view(), name="v4-show-lists"),
    path("to-do-list/create/", CreateListView.as_view(), name="v4-create-list"),
    path("to-do-list/<int:pk>/edit/", GetEditDeleteListView.as_view(), name="v4-edit-list"),
    path("to-do-list/<int:pk>/delete/", GetEditDeleteListView.as_view(), name="v4-delete-list"),
    path("to-do-list/<int:pk>/get/", GetEditDeleteListView.as_view(), name="v4-get-list"),
    path(
        "to-do-list/<int:pk>/add-shared-tasks/",
        AddSharedTaskView.as_view(),
        name="v4-add-shared-tasks",
    ),
    path("task/create/", CreateTaskView.as_view(), name="v4-create-task"),
    path("task/<int:pk>/edit/", GetEditDeleteTaskView.as_view(), name="v4-edit-task"),
    path("task/<int:pk>/get/", GetEditDeleteTaskView.as_view(), name="v4-get-task"),
    path("task/<int:pk>/delete/", GetEditDeleteTaskView.as_view(), name="v4-delete-task"),
    path("task/<int:pk>/share/", ShareTaskView.as_view(), name="v4-share-task"),
    path("task/get-shared/", GetSharedTasksView.as_view(), name="v4-get-shared-tasks"),
]
