from django.urls import path

from ToDoListApp.version4.views.create_list_view4 import CreateList4

v4_urlpatterns = [
    path("to-do-list/show-all/", ShowLists4.as_view(), name='v3-show-lists'),
    path("to-do-list/create/", CreateList4.as_view(), name='v4-create-list'),
    # path("to-do-list/<int:list_id>/edit/", EditList3.as_view(), name='v3-edit-list'),
    # path("to-do-list/<int:list_id>/delete/", DeleteList3.as_view(), name='v3-delete-list'),
    # path("to-do-list/<int:list_id>/get/", GetList3.as_view(), name='v3-get-list'),
    # path("to-do-list/<int:list_id>/task/create/", CreateTask3.as_view(), name='v3-create-task'),
    # path("to-do-list/<int:list_id>/task/<int:task_id>/edit/", EditTask3.as_view(), name='v3-edit-task'),
    # path("task/<int:task_id>/get/", GetTask3.as_view(), name='v3-get-task'),
    # path("to-do-list/<int:list_id>/task/<int:task_id>/delete/", DeleteTask3.as_view(), name='v3-delete-task'),
    # path("to-do-list/<int:list_id>/task/<int:task_id>/share/", ShareTask3.as_view(), name='v3-share-task'),
    # path("to-do-list/<int:list_id>/task/shared-tasks/", AddSharedTasks3.as_view(), name='v3-add-shared-tasks'),
]
