from django.shortcuts import render

# Create your views here.
def admin_home(request):
    view = render(request, 'index.html')
    return view