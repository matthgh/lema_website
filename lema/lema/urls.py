from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("accounts.urls")),
    path("", include("client.urls")),
    path("administration/", include("administration.urls")),
] + static(settings.STATIC_URL)
