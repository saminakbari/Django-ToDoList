from rest_framework import routers

from ToDoListApp.version6.view_sets import (
    TaskModelViewSet,
    ToDoListModelViewSet,
)

router = routers.DefaultRouter()
router.register(
    prefix=r"to-do-list", viewset=ToDoListModelViewSet, basename="to-do-list"
)
router.register(prefix=r"task", viewset=TaskModelViewSet, basename="task")
v6_urlpatterns = router.urls
