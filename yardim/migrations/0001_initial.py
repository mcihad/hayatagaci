# Generated by Django 5.1.2 on 2024-10-30 18:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Okul",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("okul_ad", models.CharField(max_length=100, verbose_name="Okul Adı")),
                (
                    "yetkili",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Yetkili"
                    ),
                ),
                (
                    "unvan",
                    models.CharField(
                        blank=True,
                        help_text="Öğretmen, Müdür, Müdür Yardımcısı vb.",
                        max_length=100,
                        null=True,
                        verbose_name="Ünvan",
                    ),
                ),
                (
                    "telefon",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Telefon"
                    ),
                ),
                (
                    "adres",
                    models.TextField(blank=True, null=True, verbose_name="Adres"),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="E-Posta"
                    ),
                ),
                ("aktif", models.BooleanField(default=True, verbose_name="Aktif")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Oluşturulma Tarihi"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Güncellenme Tarihi"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="okul",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Kantin Kullanıcısı",
                    ),
                ),
            ],
            options={
                "verbose_name": "Okul",
                "verbose_name_plural": "Okullar",
            },
        ),
        migrations.CreateModel(
            name="Ogrenci",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "kart_no",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Kart No"
                    ),
                ),
                ("ad_soyad", models.CharField(max_length=100, verbose_name="Ad Soyad")),
                (
                    "sinif",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Sınıf"
                    ),
                ),
                (
                    "telefon",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Telefon"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="E-Posta"
                    ),
                ),
                (
                    "veli",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Öğrenci Velisi",
                    ),
                ),
                (
                    "veli_telefon",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="Veli Telefon No",
                    ),
                ),
                (
                    "periyot",
                    models.IntegerField(
                        choices=[
                            (1, "Günlük"),
                            (2, "Haftalık"),
                            (3, "Aylık"),
                            (4, "Yıllık"),
                        ],
                        default=1,
                        verbose_name="Periyot",
                    ),
                ),
                (
                    "miktar",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Miktar"
                    ),
                ),
                ("aktif", models.BooleanField(default=True, verbose_name="Aktif")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Oluşturulma Tarihi"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Güncellenme Tarihi"
                    ),
                ),
                (
                    "okul",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ogrenciler",
                        to="yardim.okul",
                        verbose_name="Okul",
                    ),
                ),
            ],
            options={
                "verbose_name": "Öğrenci",
                "verbose_name_plural": "Öğrenciler",
            },
        ),
        migrations.CreateModel(
            name="Yardim",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "kart_no",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Kart No"
                    ),
                ),
                ("ad_soyad", models.CharField(max_length=100, verbose_name="Ad")),
                ("tarih", models.DateField(db_index=True, verbose_name="Tarih")),
                (
                    "miktar",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Miktar"
                    ),
                ),
                (
                    "aciklama",
                    models.TextField(blank=True, null=True, verbose_name="Açıklama"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Oluşturulma Tarihi"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Güncellenme Tarihi"
                    ),
                ),
                (
                    "ogrenci",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="yardimlar",
                        to="yardim.ogrenci",
                        verbose_name="Öğrenci",
                    ),
                ),
                (
                    "okul",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="yardimlar",
                        to="yardim.okul",
                        verbose_name="Okul",
                    ),
                ),
            ],
            options={
                "verbose_name": "Yardım",
                "verbose_name_plural": "Yardımlar",
            },
        ),
        migrations.AddIndex(
            model_name="ogrenci",
            index=models.Index(
                fields=["kart_no"], name="yardim_ogre_kart_no_f2c3df_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="ogrenci",
            index=models.Index(
                fields=["ad_soyad"], name="yardim_ogre_ad_soya_14031d_idx"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="ogrenci",
            unique_together={("okul", "kart_no")},
        ),
    ]