from django.db.models import Sum
from django.http import Http404
from django.utils import timezone
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import YardimSerializer
from yardim.models import Ogrenci, Yardim


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def yardim_ekle(request, kart_no):
    try:
        ogrenci = Ogrenci.objects.get(kart_no=kart_no, okul=request.user.okul)
    except Ogrenci.DoesNotExist:
        raise Http404
    miktar = request.data.get("miktar") or 0
    bakiye = ogrenci.bakiye
    if not ogrenci.aktif:
        raise serializers.ValidationError({"detail": "Öğrenci aktif değil."})
    if miktar <= 0:
        raise serializers.ValidationError(
            {"detail": "Miktar sıfırdan büyük olmalıdır."}
        )

    if miktar > bakiye:
        raise serializers.ValidationError(
            {"detail": "Yetersiz bakiye. Bakiye: {}".format(bakiye)}
        )

    try:
        Yardim.objects.create(
            ogrenci=ogrenci,
            miktar=miktar,
            ad_soyad=ogrenci.ad_soyad,
            tarih=timezone.datetime.now(),
            okul=request.user.okul,
            kart_no=ogrenci.kart_no,
        )
    except Exception as e:
        raise serializers.ValidationError({"detail": str(e)})
    return Response(
        {
            "detail": "Yardım başarıyla eklendi.",
            "miktar": miktar,
            "kalan": bakiye - miktar,
        }
    )


class DateRangeSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def rapor_view(request):

    serializer = DateRangeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    start_date = serializer.validated_data.get("start_date")
    end_date = serializer.validated_data.get("end_date")

    if not start_date or not end_date:
        raise serializers.ValidationError(
            {"detail": "Başlangıç ve bitiş tarihi zorunludur."}
        )

    if start_date > end_date:
        raise serializers.ValidationError(
            {"detail": "Başlangıç tarihi bitiş tarihinden büyük olamaz."}
        )

    # date range max 3 months
    if (end_date - start_date).days > 90:
        raise serializers.ValidationError(
            {"detail": "Tarih aralığı maksimum 3 ay olabilir."}
        )

    yardimlar = Yardim.objects.filter(
        tarih__range=[start_date, end_date],
        okul=request.user.okul,
    )

    yardim_serializer = YardimSerializer(yardimlar, many=True)

    return Response(yardim_serializer.data)