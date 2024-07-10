from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", include("client.urls")),
    path("administration/", include("administration.urls")),
    # path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.STATIC_URL)
