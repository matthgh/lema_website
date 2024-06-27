from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .calendar_view import CustomHTMLCalendar
from calendar import HTMLCalendar


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

    cal = CustomHTMLCalendar().formatmonth(2024, 5)
    cal1 = HTMLCalendar().formatmonth(2024, 5)

    print(cal)
    print(cal1)

    context["cal"] = cal

    print(cal)

    view = render(request, "appointment_page.html", context)
    return view
