from django.urls import path

from ToDoListApp.version5.views.task_view_set import TaskViewSet
from ToDoListApp.version5.views.to_do_list_view_set import ToDoListViewSet

v5_urlpatterns = [
    path("to-do-list/show-all/", ToDoListViewSet.as_view({'get': 'list'}),
         name='v5-show-lists'),
    path("to-do-list/create/", ToDoListViewSet.as_view({'post': 'create'}),
         name='v5-create-list'),
    path("to-do-list/<int:pk>/edit/", ToDoListViewSet.as_view({'post': 'partial_update'}),
         name='v5-edit-list'),
    path("to-do-list/<int:pk>/delete/", ToDoListViewSet.as_view({'post': 'destroy'}),
         name='v5-delete-list'),
    path("to-do-list/<int:pk>/get/", ToDoListViewSet.as_view({'get': 'retrieve'}),
         name='v5-get-list'),
    path("to-do-list/<int:pk>/add-shared-task/",
         ToDoListViewSet.as_view({'post': 'add_shared_task'}),
         name='v5-add-shared-task'),
    path("task/show-all/", TaskViewSet.as_view({'get': 'list'}), name='v5-show-tasks'),
    path("task/create/", TaskViewSet.as_view({'post': 'create'}), name='v5-create-task'),
    path("task/<int:task_id>/edit/", TaskViewSet.as_view({'post': 'partial_update'}),
         name='v5-edit-task'),
    path("task/<int:task_id>/get/", TaskViewSet.as_view({'get': 'retrieve'}),
         name='v5-get-task'),
    path("task/<int:task_id>/delete/", TaskViewSet.as_view({'post': 'destroy'}),
         name='v5-delete-task'),
    path("task/<int:task_id>/share/", TaskViewSet.as_view({'post': 'share_task'}),
         name='v5-share-task'),
    path("task/get-shared/", TaskViewSet.as_view({'get': 'get_shared_tasks'}), name='v5-get-shared-tasks'),
]
