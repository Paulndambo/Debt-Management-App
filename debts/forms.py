from django import forms

from .models import MoneyLoanPayment, ItemLoanPayment, LoanApplication

class MoneyLoanPaymentForm(forms.ModelForm):
    class Meta:
        model = MoneyLoanPayment
        fields = "__all__"


class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ["customer", "amount_applied"]

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'amount_applied': forms.NumberInput(attrs={'class': 'form-control'}),
        }
