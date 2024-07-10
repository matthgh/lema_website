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

from .forms import *

from .forms import UserInfoForm


def home(request):
    context = {
        "full_star": config("FULL_STAR"),
        "outline_star": config("OUTLINE_STAR"),
        "image_1": config("IMAGE_1"),
        "image_2": config("IMAGE_2"),
        "image_3": config("IMAGE_3"),
        "home_img": config("HOME_IMG"),
    }
    view = render(request, "home.html", context)
    return view


def gallery(request):
    context = {
        "tagli": [
            config("TAGLIO_1"),
            config("TAGLIO_2"),
            config("TAGLIO_3"),
            config("TAGLIO_4"),
            config("TAGLIO_5"),
            config("TAGLIO_6"),
            config("TAGLIO_7"),
            config("TAGLIO_8"),
            config("TAGLIO_9"),
            config("TAGLIO_10"),
            config("TAGLIO_11"),
            config("TAGLIO_12"),
            config("TAGLIO_13"),
            config("TAGLIO_14"),
            config("TAGLIO_15"),
            config("TAGLIO_16"),
            config("TAGLIO_17"),
            config("TAGLIO_18"),
            config("TAGLIO_19"),
            config("TAGLIO_20"),
            config("TAGLIO_21"),
            config("TAGLIO_22"),
            config("TAGLIO_23"),
            config("TAGLIO_24"),
        ]
    }
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
    request.session["time_selection"] = request.POST.get("selection")
    day = request.session["set_day"]
    month = request.session["set_month"]
    year = request.session["set_year"]

    print(request.session["time_selection"])

    context = {
        "user_form": UserInfoForm(),
        "time": request.session["time_selection"],
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
        phone_number = request.POST.get("phone_number")
        print(phone_number)

        if user_info.is_valid():
            user = UserInfo.objects.get(phone_number=phone_number)

            if not user:
                user = user_info.save()

            for form_class in form_options:

                if form_class().time == request.session["time_selection"]:

                    date = f"{year}-{month}-{day}"
                    dictionary = {"user_info": user.pk, "date": date}
                    q_dictionary = QueryDict(
                        urlencode(dictionary, doseq=True), mutable=True
                    )
                    form = form_class(q_dictionary)

                    if form.is_valid():
                        print("valida")
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
