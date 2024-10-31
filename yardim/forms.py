from django import forms
from .models import Okul


class SearchForm(forms.Form):
    start_date = forms.DateField(
        label="Başlangıç Tarihi", widget=forms.DateInput(attrs={"type": "date"})
    )
    end_date = forms.DateField(
        label="Bitiş Tarihi", widget=forms.DateInput(attrs={"type": "date"})
    )
    school = forms.ModelChoiceField(queryset=Okul.objects.all(), label="Okul")
    grouping = forms.BooleanField(label="Tarihe Göre Grupla", required=False)

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError(
                "Başlangıç tarihi bitiş tarihinden büyük olamaz."
            )

        # en fazla 3 ay olabilir aralık
        if start_date and end_date and (end_date - start_date).days > 90:
            raise forms.ValidationError("Aralık en fazla 3 ay olabilir.")

        return cleaned_data
