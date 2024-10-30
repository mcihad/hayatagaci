from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .viewsets import OgrenciRetrieveViewByKartNo
from .views import yardim_ekle, rapor_view

router = routers.DefaultRouter()
# router.register(r"ogrenci", OgrenciViewSet)

urlpatterns = router.urls + [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("ogrenci/<str:kart_no>/", OgrenciRetrieveViewByKartNo.as_view()),
    path("ogrenci/<str:kart_no>/create/", yardim_ekle),
    path("kantin/rapor/", rapor_view),
]
