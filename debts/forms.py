from django import forms

from .models import MoneyLoanPayment, ItemLoanPayment

class MoneyLoanPaymentForm(forms.ModelForm):
    class Meta:
        model = MoneyLoanPayment
        fields = "__all__"