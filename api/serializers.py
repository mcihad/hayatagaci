from rest_framework import serializers
from yardim.models import Ogrenci, Yardim


class OgrenciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ogrenci
        fields = "__all__"


class YardimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yardim
        fields = ["kart_no", "ad_soyad", "tarih", "miktar"]


class GroupedYardimSerializer(serializers.Serializer):
    tarih = serializers.DateField()
    total = serializers.DecimalField(decimal_places=2, max_digits=10)
