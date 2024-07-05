from django.shortcuts import get_list_or_404, render
from django.http import Http404
from client.models import (
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

import datetime


# Create your views here.
def admin_home(request):
    context = {}
    view = render(request, "index.html", context)
    return view


def accordion(request):
    date = request.GET.get("date") or datetime.date.today()
    context = {
        "user_info": UserInfo,
    }

    classes = [
        Eight.objects.filter(date=date),
        HalfEight.objects.filter(date=date),
        Nine.objects.filter(date=date),
        HalfNine.objects.filter(date=date),
        Ten.objects.filter(date=date),
        HalfTen.objects.filter(date=date),
        Eleven.objects.filter(date=date),
        HalfEleven.objects.filter(date=date),
        Two.objects.filter(date=date),
        HalfTwo.objects.filter(date=date),
        Three.objects.filter(date=date),
        HalfThree.objects.filter(date=date),
        Four.objects.filter(date=date),
        HalfFour.objects.filter(date=date),
        Five.objects.filter(date=date),
        HalfFive.objects.filter(date=date),
    ]

    # objects = []
    # for _class in classes:
    #     obj = list(_class.objects.filter(date=date))
    #     objects.append(obj)

    # context["objects"] = objects
    context["classes"] = classes

    view = render(request, "partials/accordion.html", context)

    return view
