from django.urls import path

from ToDoListApp.version5.views.to_do_list_view_set import ToDoListViewSet

v5_urlpatterns = [
    path("to-do-list/show-all/", ToDoListViewSet.as_view({'get': 'list'}), name='v5-show-lists'),
    path("to-do-list/create/", ToDoListViewSet.as_view({'post': 'create'}), name='v5-create-list'),
    # path("to-do-list/<int:id>/edit/", EditList5.as_view(), name='v5-edit-list'),
    # path("to-do-list/<int:id>/delete/", DeleteList5.as_view(), name='v5-delete-list'),
    path("to-do-list/<int:pk>/get/", ToDoListViewSet.as_view({'get': 'retrieve'}), name='v5-get-list'),
    # path("to-do-list/<int:id>/task/create/", CreateTask5.as_view(),
    #      name='v5-create-task'),
    # path("task/<int:id>/edit/", EditTask5.as_view(), name='v5-edit-task'),
    # path("task/<int:id>/get/", GetTask5.as_view(), name='v5-get-task'),
    # path("to-do-list/<int:list_id>/task/<int:id>/delete/",
    #      DeleteTask5.as_view(), name='v5-delete-task'),
    # path("task/<int:id>/share/", ShareTask5.as_view(), name='v5-share-task'),
    # path("to-do-list/<int:id>/add-shared-tasks/", AddSharedTask5.as_view(),
    #      name='v5-add-shared-tasks'),
    # path("task/get/shared/", GetSharedTasks5.as_view(), name='v5-get-shared-tasks'),
]
