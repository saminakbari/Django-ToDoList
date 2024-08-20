from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from ToDoList import settings
from ToDoListApp.urls import v1_urlpatterns
from ToDoListApp.version2.urls import v2_urlpatterns
from ToDoListApp.version3.urls import v3_urlpatterns
from ToDoListApp.version4.urls import v4_urlpatterns
from ToDoListApp.version5.urls import v5_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_url'),
    path("v1/", include(v1_urlpatterns)),
    path("v2/", include(v2_urlpatterns)),
    path("v3/", include(v3_urlpatterns)),
    path("v4/", include(v4_urlpatterns)),
    path("v5/", include(v5_urlpatterns))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
