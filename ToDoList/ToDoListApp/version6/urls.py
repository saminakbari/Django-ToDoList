from rest_framework import routers

from ToDoListApp.version6.view_sets.task_model_view_set import TaskModelViewSet
from ToDoListApp.version6.view_sets.to_do_list_model_view_set import (
    ToDoListModelViewSet,
)

router = routers.DefaultRouter()
router.register(
    prefix=r"to-do-list", viewset=ToDoListModelViewSet, basename="to-do-list"
)
router.register(prefix=r"task", viewset=TaskModelViewSet, basename="task")
v6_urlpatterns = router.urls
