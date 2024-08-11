from django.urls import path

from .views.add_shared_tasks_view2 import AddSharedTasks
from .views.create_list_view2 import CreateList
from .views.create_task_view2 import CreateTask
from .views.delete_list_view2 import DeleteList
from .views.delete_task_view2 import DeleteTask
from .views.edit_list_view2 import EditList
from .views.edit_task_view2 import EditTask
from .views.get_list_view2 import GetList
from .views.get_task_view2 import GetTask
from .views.login_view2 import Login
from .views.register_login_view2 import RegisterLogin
from .views.register_view2 import Register
from .views.share_task_view2 import ShareTask
from .views.show_lists_view2 import ShowLists

v2_urlpatterns = [
    path("to-do-list/app/opening/", RegisterLogin.as_view()),
    path("user/register/", Register.as_view()),
    path("user/login/", Login.as_view()),
    path("to-do-list/showall/<str:username>/", ShowLists.as_view()),
    path("to-do-list/create/<str:username>/", CreateList.as_view()),
    path("to-do-list/edit/<int:list_id>/<str:username>/", EditList.as_view()),
    path("to-do-list/delete/<int:list_id>/<str:username>/", DeleteList.as_view()),
    path("to-do-list/get/<int:list_id>/", GetList.as_view()),
    path("task/create/<int:list_id>/", CreateTask.as_view()),
    path("task/edit/<int:task_id>/<int:list_id>/", EditTask.as_view()),
    path("task/delete/<int:task_id>/<int:list_id>/", DeleteTask.as_view()),
    path("task/get/<int:task_id>/", GetTask.as_view()),
    path("task/share/<int:task_id>/", ShareTask.as_view()),
    path("task/shared-tasks/<str:username>/<int:list_id>/", AddSharedTasks.as_view()),
]
