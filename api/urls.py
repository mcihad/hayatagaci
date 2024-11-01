from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .viewsets import OgrenciRetrieveViewByKartNo
from .views import (
    yardim_create,
    report_view_by_date_range,
    report_view_by_date,
    report_by_group,
)

router = routers.DefaultRouter()
# router.register(r"ogrenci", OgrenciViewSet)

urlpatterns = router.urls + [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("ogrenci/<str:kart_no>/", OgrenciRetrieveViewByKartNo.as_view()),
    path("ogrenci/<str:kart_no>/create/", yardim_create),
    path("kantin/rapor/range/", report_view_by_date_range),
    path("kantin/rapor/date/", report_view_by_date),
    path("kantin/rapor/group/", report_by_group),
]
