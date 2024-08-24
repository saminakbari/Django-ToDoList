from rest_framework import routers

from ToDoListApp.version5.view_sets.task_view_set import TaskViewSet
from ToDoListApp.version5.view_sets.to_do_list_view_set import ToDoListViewSet

router = routers.DefaultRouter()
router.register(r"to-do-list", ToDoListViewSet, basename="to-do-list")
router.register(r"task", TaskViewSet, basename="task")
v5_urlpatterns = router.urls
