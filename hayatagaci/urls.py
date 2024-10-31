from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls
from yardim import views as yardim_views


def index(request):
    return HttpResponse("Under construction")


urlpatterns = [
    path("", index),
    path("report/", yardim_views.report, name="yardim_report"),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
