from django.urls import path

from ToDoListApp.version1.views import (
    add_shared_tasks_view,
    create_list_view,
    create_task_view,
    delete_list_view,
    delete_task_view,
    edit_list_view,
    edit_task_view,
    get_list_view,
    get_task_view,
    share_task_view,
    show_all_lists_view,
)

v1_urlpatterns = [
    path("to-do-list/show-all/", show_all_lists_view, name="v1-show-lists"),
    path("to-do-list/create/", create_list_view, name="v1-create-list"),
    path("to-do-list/<int:list_id>/edit/", edit_list_view, name="v1-edit-list"),
    path("to-do-list/<int:list_id>/delete/", delete_list_view, name="v1-delete-list"),
    path("to-do-list/<int:list_id>/get/", get_list_view, name="v1-get-list"),
    path(
        "to-do-list/<int:list_id>/task/create/", create_task_view, name="v1-create-task"
    ),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/edit/",
        edit_task_view,
        name="v1-edit-task",
    ),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/delete/",
        delete_task_view,
        name="v1-delete-task",
    ),
    path("task/<int:task_id>/get/", get_task_view, name="v1-get-task"),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/share/",
        share_task_view,
        name="v1-share-task",
    ),
    path(
        "to-do-list/<int:list_id>/shared-tasks/",
        add_shared_tasks_view,
        name="v1-add-shared-tasks",
    ),
]
