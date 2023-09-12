from django import forms
from lipalater.models import LipaLaterLoan


class LipaLaterLoanForm(forms.ModelForm):
    class Meta:
        model = LipaLaterLoan
        fields = ["customer", "item"]

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'item': forms.Select(attrs={'class': 'form-control'}),
        }