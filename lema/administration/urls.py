from django.urls import path
from . import views

app_name = "administration"

urlpatterns = [
    path("", views.admin_home, name="admin-page"),
    path("accordion/", views.accordion, name="accordion-htmx"),
]
