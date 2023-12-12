from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = "home"),
    path('update-showcase', update_showcase, name = "update_showcase"),
    path("login/", login_user, name ="login"),
    path("logout/", logout_user, name ="logout"),
    path("register/", register_user, name ="register"),
]
