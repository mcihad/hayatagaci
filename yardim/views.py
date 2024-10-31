from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from .models import Yardim
from .forms import SearchForm


# login required and admin required
@user_passes_test(lambda u: u.is_superuser)
def report(request):
    form = SearchForm(request.POST or None)
    data = {}
    total = 0
    is_grouping = False
    if form.is_valid():
        start_date = form.cleaned_data["start_date"]
        end_date = form.cleaned_data["end_date"]
        school = form.cleaned_data["school"]
        grouping = form.cleaned_data["grouping"]
        is_grouping = grouping
        if is_grouping:
            data = (
                Yardim.objects.filter(
                    tarih__gte=start_date,
                    tarih__lte=end_date,
                    okul=school,
                )
                .values("tarih")
                .annotate(total=Sum("miktar"))
            )

            print(data)
        else:
            data = (
                Yardim.objects.filter(
                    tarih__gte=start_date,
                    tarih__lte=end_date,
                    okul=school,
                )
                .values("ad_soyad", "tarih", "miktar", "aciklama")
                .order_by("-tarih")
            )

        total = (
            Yardim.objects.filter(
                tarih__gte=start_date, tarih__lte=end_date, okul=school
            ).aggregate(Sum("miktar"))["miktar__sum"]
            or 0
        )
    return render(
        request,
        "yardim/report/index.html",
        context={
            "form": form,
            "data": data,
            "is_grouping": is_grouping,
            "total": total,
        },
    )
