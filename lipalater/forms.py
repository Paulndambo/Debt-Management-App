from django import forms
from lipalater.models import LipaLaterLoan


class LipaLaterLoanForm(forms.ModelForm):
    class Meta:
        model = LipaLaterLoan
        fields = ["customer", ""]