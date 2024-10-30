from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils import timezone


class Okul(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="okul",
        verbose_name="Kantin Kullanıcısı",
    )
    okul_ad = models.CharField("Okul Adı", max_length=100)
    yetkili = models.CharField("Yetkili", max_length=100, blank=True, null=True)
    unvan = models.CharField(
        "Ünvan",
        max_length=100,
        blank=True,
        null=True,
        help_text="Öğretmen, Müdür, Müdür Yardımcısı vb.",
    )
    telefon = models.CharField("Telefon", max_length=20, blank=True, null=True)
    adres = models.TextField("Adres", blank=True, null=True)
    email = models.EmailField("E-Posta", blank=True, null=True)
    aktif = models.BooleanField("Aktif", default=True)

    created_at = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)
    updated_at = models.DateTimeField("Güncellenme Tarihi", auto_now=True)

    def __str__(self):
        return self.okul_ad

    class Meta:
        verbose_name = "Okul"
        verbose_name_plural = "Okullar"


class YardimPeriyotChoices(models.IntegerChoices):
    GUNLUK = 1, "Günlük"
    HAFTALIK = 2, "Haftalık"
    AYLIK = 3, "Aylık"
    YILLIK = 4, "Yıllık"


class Ogrenci(models.Model):
    okul = models.ForeignKey(
        Okul,
        on_delete=models.CASCADE,
        related_name="ogrenciler",
        verbose_name="Okul",
    )
    kart_no = models.CharField("Kart No", max_length=100, blank=True, null=True)
    ad_soyad = models.CharField("Ad Soyad", max_length=100)

    sinif = models.CharField("Sınıf", max_length=20, blank=True, null=True)
    telefon = models.CharField("Telefon", max_length=20, blank=True, null=True)
    email = models.EmailField("E-Posta", blank=True, null=True)
    veli = models.CharField("Öğrenci Velisi", max_length=100, blank=True, null=True)
    veli_telefon = models.CharField(
        "Veli Telefon No", max_length=20, blank=True, null=True
    )
    periyot = models.IntegerField(
        "Periyot",
        choices=YardimPeriyotChoices.choices,
        default=YardimPeriyotChoices.GUNLUK,
    )
    miktar = models.DecimalField("Miktar", max_digits=10, decimal_places=2)
    aktif = models.BooleanField("Aktif", default=True)

    created_at = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)
    updated_at = models.DateTimeField("Güncellenme Tarihi", auto_now=True)

    @property
    def bakiye(self):
        kalan = 0
        if self.periyot == YardimPeriyotChoices.GUNLUK:
            yardim = (
                Yardim.objects.filter(
                    ogrenci=self,
                    tarih=timezone.datetime.now().date(),
                ).aggregate(Sum("miktar"))["miktar__sum"]
                or 0
            )
            kalan = self.miktar - yardim
        elif self.periyot == YardimPeriyotChoices.AYLIK:
            yardim = (
                Yardim.objects.filter(
                    ogrenci=self,
                    tarih__month=timezone.datetime.now().month,
                    tarih__year=timezone.datetime.now().year,
                ).aggregate(Sum("miktar"))["miktar__sum"]
                or 0
            )
            kalan = self.miktar - yardim

        elif self.periyot == YardimPeriyotChoices.YILLIK:
            yardim = (
                Yardim.objects.filter(
                    ogrenci=self,
                    tarih__year=timezone.datetime.now().year,
                ).aggregate(Sum("miktar"))["miktar__sum"]
                or 0
            )
            kalan = self.miktar - yardim
        return kalan

    def __str__(self):
        return self.ad_soyad

    class Meta:
        verbose_name = "Öğrenci"
        verbose_name_plural = "Öğrenciler"

        indexes = [
            models.Index(fields=["kart_no"]),
            models.Index(fields=["ad_soyad"]),
        ]

        unique_together = [
            ["okul", "kart_no"],
        ]


class Yardim(models.Model):
    okul = models.ForeignKey(
        Okul,
        on_delete=models.CASCADE,
        related_name="yardimlar",
        verbose_name="Okul",
        editable=False,
    )

    ogrenci = models.ForeignKey(
        Ogrenci,
        on_delete=models.CASCADE,
        related_name="yardimlar",
        verbose_name="Öğrenci",
    )
    kart_no = models.CharField("Kart No", max_length=100, blank=True, null=True)
    ad_soyad = models.CharField("Ad", max_length=100)

    tarih = models.DateField("Tarih", db_index=True)
    miktar = models.DecimalField("Miktar", max_digits=10, decimal_places=2)
    aciklama = models.TextField("Açıklama", blank=True, null=True)

    created_at = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)
    updated_at = models.DateTimeField("Güncellenme Tarihi", auto_now=True)

    def __str__(self):
        return f"{self.ogrenci.ad_soyad} - {self.tarih}"

    class Meta:
        verbose_name = "Yardım"
        verbose_name_plural = "Yardımlar"
