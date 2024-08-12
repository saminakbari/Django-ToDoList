from django.contrib import admin
from django.urls import path, include

from my_app.urls import v1_urlpatterns
from my_app.version3.urls import v3_urlpatterns
from my_app.views.login_view import login_user
from my_app.views.register_view import register_user
from my_app.views.create_list_view import create_list
from my_app.views.create_task_view import create_task
from my_app.views.delete_list_view import delete_list
from my_app.views.delete_task_view import delete_task
from my_app.views.edit_list_view import edit_to_do_list
from my_app.views.edit_task_view import edit_task
from my_app.views.get_list_view import get_list
from my_app.views.get_task_view import get_task
from my_app.views.share_task_view import share_task
from my_app.views.add_shared_tasks_view import add_shared_tasks
from my_app.views.show_all_lists_view import show_all_lists
from my_app.version2 import v2_urlpatterns
from my_app.views.register_login_view import register_or_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path("v1/", include(v1_urlpatterns)),
    path("v2/", include(v2_urlpatterns)),
    path("v3/", include(v3_urlpatterns))
]
