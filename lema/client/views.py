from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .calendar_view import CustomHTMLCalendar
from calendar import HTMLCalendar
from datetime import date


# @login_required
def home(request):
    context = {}
    view = render(request, "home.html", context)
    return view


def gallery(request):
    context = {}
    view = render(request, "gallery.html", context)
    return view


def appointment_page(request):
    context = {}
    request.session["set_month"] = date.today().month
    request.session["set_year"] = date.today().year

    cal = CustomHTMLCalendar().formatmonth(
        request.session["set_year"], request.session["set_month"]
    )
    context["cal"] = cal
    view = render(request, "appointment_page.html", context)
    return view


def appointment_page_htmx(request):
    context = {}

    if request.method == "POST":
        if request.session["set_month"] + 1 > 12:
            request.session["set_month"] = 1
            request.session["set_month"] += 1
        else:
            request.session["set_month"] += 1

    cal = CustomHTMLCalendar().formatmonth(
        request.session["set_year"], request.session["set_month"]
    )

    context["cal"] = cal
    view = render(request, "partials/appointment_calendar.html", context)

    return view
