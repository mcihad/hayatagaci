from django.contrib import admin
from .models import Okul, Ogrenci, Yardim
from .views import report


@admin.register(Okul)
class OkulAdmin(admin.ModelAdmin):
    list_display = ["okul_ad", "yetkili", "unvan", "telefon", "aktif"]
    list_filter = ["aktif"]
    autocomplete_fields = ["user"]
    readonly_fields = ["created_at", "updated_at"]
    search_fields = [
        "okul_ad",
        "yetkili",
        "telefon",
        "user__username",
        "user__first_name",
        "user__last_name",
    ]
    list_select_related = ["user"]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "okul_ad",
                    "yetkili",
                    "unvan",
                    "telefon",
                    "adres",
                    "email",
                    "aktif",
                )
            },
        ),
        (
            "Oluşturulma ve Güncellenme Tarihleri",
            {"fields": ("created_at", "updated_at"), "classes": ["collapse"]},
        ),
    )


@admin.register(Ogrenci)
class OgrenciAdmin(admin.ModelAdmin):
    list_display = [
        "ad_soyad",
        "kart_no",
        "okul",
        "sinif",
        "telefon",
        "email",
        "periyot",
        "miktar",
        "aktif",
    ]

    list_filter = ["okul", "periyot", "aktif"]
    search_fields = [
        "ad_soyad",
        "kart_no",
    ]
    list_select_related = ["okul"]
    readonly_fields = ["created_at", "updated_at"]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "okul",
                    "kart_no",
                    "ad_soyad",
                    "sinif",
                    "telefon",
                    "email",
                )
            },
        ),
        ("Yardım Bilgileri", {"fields": ("periyot", "miktar", "aktif")}),
        ("Veli Bilgileri", {"fields": ("veli", "veli_telefon")}),
        (
            "Oluşturulma ve Güncellenme Tarihleri",
            {"fields": ("created_at", "updated_at"), "classes": ["collapse"]},
        ),
    )


@admin.register(Yardim)
class YardimAdmin(admin.ModelAdmin):
    list_display = ["okul", "ogrenci", "tarih", "miktar", "aciklama"]
    list_filter = ["okul", "tarih"]
    search_fields = ["ogrenci__ad_soyad", "ogrenci__kart_no"]
    list_select_related = ["okul", "ogrenci"]
    readonly_fields = ["created_at", "updated_at"]


admin.site.site_header = "Hayat Ağacı Yönetim Paneli"
admin.site.site_title = "Hayat Ağacı"
admin.site.index_title = "Yönetim Paneli"
