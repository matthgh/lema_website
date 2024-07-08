from urllib.parse import urlencode
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.conf import settings
from django.http import QueryDict
from sms import send_sms
from decouple import config

from .calendar_view import Custom2HTMLCalendar
from datetime import date as dt

from .forms import (
    EightForm,
    HalfEightForm,
    NineForm,
    HalfNineForm,
    TenForm,
    HalfTenForm,
    ElevenForm,
    HalfElevenForm,
    TwoForm,
    HalfTwoForm,
    ThreeForm,
    HalfThreeForm,
    FourForm,
    HalfFourForm,
    FiveForm,
    HalfFiveForm,
)

from .forms import UserInfoForm


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
    request.session["set_month"] = dt.today().month
    request.session["set_year"] = dt.today().year

    cal = Custom2HTMLCalendar().formatmonth(
        request.session["set_year"], request.session["set_month"]
    )
    context["cal"] = cal
    context["booking_appoints_url"] = config("BOOKING_APPOINTS_URL")
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

        elif arrow == "current_day":
            request.session["set_month"] = dt.today().month
            request.session["set_year"] = dt.today().year

    request.session["set_year"], request.session["set_month"]

    cal = Custom2HTMLCalendar().formatmonth(
        request.session["set_year"], request.session["set_month"]
    )

    context["cal"] = cal
    view = render(request, "partials/appointment_calendar.html", context)

    return view


def day_htmx(request, day):
    context = {
        "options": [
            EightForm(),
            HalfEightForm(),
            NineForm(),
            HalfNineForm(),
            TenForm(),
            HalfTenForm(),
            ElevenForm(),
            HalfElevenForm(),
            TwoForm(),
            HalfTwoForm(),
            ThreeForm(),
            HalfThreeForm(),
            FourForm(),
            HalfFourForm(),
            FiveForm(),
            HalfFiveForm(),
        ],
        "day": day,
        "max_users": settings.MAX_USERS,
    }

    view = render(request, "partials/available_option.html", context)

    return view


def show_modal(request):
    request.session["set_day"] = request.POST.get("day")
    selection = request.POST.get("selection")
    day = request.session["set_day"]
    month = request.session["set_month"]
    year = request.session["set_year"]

    context = {
        "user_form": UserInfoForm(),
        "time": selection,
        "day": request.session["set_day"],
        "month": request.session["set_month"],
        "year": request.session["set_year"],
    }

    form_options = [
        EightForm,
        HalfEightForm,
        NineForm,
        HalfNineForm,
        TenForm,
        HalfTenForm,
        ElevenForm,
        HalfElevenForm,
        TwoForm,
        HalfTwoForm,
        ThreeForm,
        HalfThreeForm,
        FourForm,
        HalfFourForm,
        FiveForm,
        HalfFiveForm,
    ]
    
    

    if request.method == "POST" and request.POST.get("type") == "submit":
        user_info = UserInfoForm(request.POST)

        if user_info.is_valid():
            user = user_info.save()

            for form_class in form_options:

                if form_class().time == selection:
                    date = f"{year}-{month}-{day}"
                    dictionary = {"user_info": user.pk, "date": date}
                    q_dictionary = QueryDict(
                        urlencode(dictionary, doseq=True), mutable=True
                    )
                    form = form_class(q_dictionary)

                    if form.is_valid():
                        form.save()
                        print("salvato")
                        messages.success(request, "Prenotazione salvata con successo!")
                    else:
                        messages.warning(request, form.errors)

        else:
            context["user_form"] = user_info
            context["errors"] = user_info.errors

        view = render(request, "partials/show-modal.html", context)
        return view

    return render(request, "partials/show-modal.html", context)
