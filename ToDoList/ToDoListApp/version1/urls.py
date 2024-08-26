from django.urls import path

from ToDoListApp.version1.views import (
    add_shared_tasks,
    create_list,
    create_task,
    delete_list,
    delete_task,
    edit_list,
    edit_task,
    get_list,
    get_task,
    share_task,
    show_all_lists,
)

v1_urlpatterns = [
    path("to-do-list/show-all/", show_all_lists, name="v1-show-lists"),
    path("to-do-list/create/", create_list, name="v1-create-list"),
    path("to-do-list/<int:list_id>/edit/", edit_list, name="v1-edit-list"),
    path("to-do-list/<int:list_id>/delete/", delete_list, name="v1-delete-list"),
    path("to-do-list/<int:list_id>/get/", get_list, name="v1-get-list"),
    path("to-do-list/<int:list_id>/task/create/", create_task, name="v1-create-task"),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/edit/",
        edit_task,
        name="v1-edit-task",
    ),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/delete/",
        delete_task,
        name="v1-delete-task",
    ),
    path("task/<int:task_id>/get/", get_task, name="v1-get-task"),
    path(
        "to-do-list/<int:list_id>/task/<int:task_id>/share/",
        share_task,
        name="v1-share-task",
    ),
    path(
        "to-do-list/<int:list_id>/shared-tasks/",
        add_shared_tasks,
        name="v1-add-shared-tasks",
    ),
]
