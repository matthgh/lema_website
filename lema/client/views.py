from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required
def home(request):
    context = {}
    view = render(request, "home.html", context)
    return view


def gallery(request):
    context = {}
    view = render(request, "gallery.html", context)
    return view
