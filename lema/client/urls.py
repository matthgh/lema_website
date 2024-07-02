from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("galleria/", views.gallery, name="gallery"),
    path("appuntamento/", views.appointment_page, name="appointment-page"),
    path("calendar/", views.appointment_page_htmx, name="appointment-calendar"),
    path("day/<int:day>", views.day_htmx, name="day-htmx"),
]
