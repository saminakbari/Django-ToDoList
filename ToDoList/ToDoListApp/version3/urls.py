from django.urls import path

from ToDoListApp.version3.views import RegisterLogin3, Register3, Login3, ShowLists3, CreateList3, EditList3, DeleteList3, \
    GetList3, CreateTask3, EditTask3, DeleteTask3, GetTask3, ShareTask3, AddSharedTasks3

v3_urlpatterns = [
    # path("to-do-list/app/opening/", RegisterLogin3.as_view(), name='opening'),
    path("to-do-list/showall/", ShowLists3.as_view()),
    path("to-do-list/create/", CreateList3.as_view()),
    path("to-do-list/edit/<int:list_id>/", EditList3.as_view()),
    path("to-do-list/delete/<int:list_id>/", DeleteList3.as_view()),
    path("to-do-list/get/<int:list_id>/", GetList3.as_view()),
    path("task/create/<int:list_id>/", CreateTask3.as_view()),
    # path("task/edit/<int:task_id>/<int:list_id>/", EditTask3.as_view()),
    # path("task/delete/<int:task_id>/<int:list_id>/", DeleteTask3.as_view()),
    # path("task/get/<int:task_id>/", GetTask3.as_view()),
    # path("task/share/<int:task_id>/", ShareTask3.as_view()),
    # path("task/shared-tasks/<str:username>/<int:list_id>/", AddSharedTasks3.as_view()),
]
