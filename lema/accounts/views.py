from django.shortcuts import render

# Create your views here.
def login_page(request):
    view = render(request, 'login_page.html')
    return view