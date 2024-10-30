from rest_framework import serializers
from yardim.models import Ogrenci, Yardim


class OgrenciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ogrenci
        fields = "__all__"


class YardimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yardim
        fields = "__all__"
