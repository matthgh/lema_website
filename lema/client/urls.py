from django.urls import path
from . import views


htmx_urlpatterns = [
    path("calendar/", views.appointment_page_htmx, name="appointment-calendar")
]


urlpatterns = [
    path("", views.home, name="home"),
    path("galleria/", views.gallery, name="gallery"),
    path("appuntamento/", views.appointment_page, name="appointment-page"),
] + htmx_urlpatterns
