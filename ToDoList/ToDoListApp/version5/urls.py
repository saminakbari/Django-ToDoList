from rest_framework import routers

from ToDoListApp.version5.view_sets import TaskViewSet, ToDoListViewSet

router = routers.DefaultRouter()
router.register(r"to-do-list", ToDoListViewSet, basename="to-do-list")
router.register(r"task", TaskViewSet, basename="task")
v5_urlpatterns = router.urls
