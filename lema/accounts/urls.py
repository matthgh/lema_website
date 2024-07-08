from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_page, name="login-page"),
    path("logout/", views.logout_page, name="logout-page"),
]
