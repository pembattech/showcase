from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = "home"),
    path('update-showcase', update_showcase, name = "update_showcase"),
    path('new', add_project, name = "new"),
    path('delete_project/<int:project_id>/', delete_project, name='delete_project'),
    path("login/", login_user, name ="login"),
    path("logout/", logout_user, name ="logout"),
]
