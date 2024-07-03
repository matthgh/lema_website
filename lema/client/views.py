from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.http import HttpResponseRedirect

from .calendar_view import CustomHTMLCalendar
from calendar import HTMLCalendar
from datetime import date

from .forms import EightForm

from .models import (
    UserInfo,
    Eight,
    HalfEight,
    Nine,
    HalfNine,
    Ten,
    HalfTen,
    Eleven,
    HalfEleven,
    Two,
    HalfTwo,
    Three,
    HalfThree,
    Four,
    HalfFour,
    Five,
    HalfFive,
)

from .forms import UserInfoForm


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
        print(request.POST)
        arrow = request.POST.get("arrow")

        if arrow == "right":
            if request.session["set_month"] + 1 > 12:
                request.session["set_month"] = 1
                request.session["set_year"] += 1
            else:
                request.session["set_month"] += 1

        elif arrow == "left":
            if request.session["set_month"] - 1 < 1:
                request.session["set_month"] = 12
                request.session["set_year"] -= 1
            else:
                request.session["set_month"] -= 1

    cal = CustomHTMLCalendar().formatmonth(
        request.session["set_year"], request.session["set_month"]
    )

    context["cal"] = cal
    view = render(request, "partials/appointment_calendar.html", context)

    return view


def day_htmx(request, day):
    context = {
        "options": [
            Eight,
            HalfEight,
            Nine,
            HalfNine,
            Ten,
            HalfTen,
            Eleven,
            HalfEleven,
            Two,
            HalfTwo,
            Three,
            HalfThree,
            Four,
            HalfFour,
            Five,
            HalfFive,
        ],
        "day": day,
    }

    view = render(request, "partials/available_option.html", context)

    return view


def show_modal(request, time):
    request.session["set_day"] = request.POST.get("day")
    context = {
        "user_form": UserInfoForm(),
        "time": time,
        "day": request.session["set_day"],
        "month": request.session["set_month"],
        "year": request.session["set_year"],
    }
    options = [
        Eight,
        HalfEight,
        Nine,
        HalfNine,
        Ten,
        HalfTen,
        Eleven,
        HalfEleven,
        Two,
        HalfTwo,
        Three,
        HalfThree,
        Four,
        HalfFour,
        Five,
        HalfFive,
    ]
    if request.method == "POST" and request.POST.get("type") == "submit":
        user_info = UserInfoForm(request.POST)
        context["user_form"] = user_info
        context["errors"] = user_info.errors

        return render(request, "partials/show-modal.html", context)

    return render(request, "partials/show-modal.html", context)


# @require_http_methods(["POST"])
# def handle_appointments_htmx(request):
#     context = {"user_form": UserInfoForm()}
#     if request.method == "POST":
#         user_form = UserInfoForm(request.POST)
#         if user_form.is_valid():
#             print("form valid")
#             # view = render(request, "partials/show-modal.html", context)
#             return render(request, "partials/show-modal.html", context)
#         else:
#             user_form = UserInfoForm(request.POST)
#             context["errors"] = user_form.errors
#             print("errore")
#             return render(request, "partials/show-modal.html", context)

#     # return render(request, "partials/show-modal.html", context)
