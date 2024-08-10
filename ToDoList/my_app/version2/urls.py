from django.urls import path

from .views.register_login_view2 import RegisterLogin
from .views.register_view2 import Register

v2_urlpatterns = [
    path("to-do-list/app/opening/", RegisterLogin.as_view()),
    path("user/register/", Register.as_view()),
    # path("user/login/", Login.as_view()),
]
