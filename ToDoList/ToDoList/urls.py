from django.contrib import admin
from django.urls import path, include

from my_app.urls import v1_urlpatterns
from my_app.version2 import v2_urlpatterns
from my_app.version3.urls import v3_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("v1/", include(v1_urlpatterns)),
    path("v2/", include(v2_urlpatterns)),
    path("v3/", include(v3_urlpatterns))
]
