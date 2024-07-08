from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from .forms import LoginViewForm


def login_page(request):
    if request.user.is_authenticated:
        return redirect("client:home")

    context = {"login_form": LoginViewForm()}

    if request.method == "POST":
        form = LoginViewForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("logged in")
                return redirect(reverse("administration:admin-page"))

    view = render(request, "login_page.html", context)
    return view


# @require_http_methods(["POST"])
@login_required()
def logout_page(request):
    logout(request)
    return redirect("client:home")
