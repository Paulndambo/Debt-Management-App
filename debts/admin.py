from django.contrib import admin
from .models import (
    LoanApplication, ItemBorrowed, ItemLoanPayment,
    CustomerItemLoan, CustomerMoneyLoan, MoneyLoanPayment
)
# Register your models here.
admin.site.register(LoanApplication)
admin.site.register(ItemBorrowed)
admin.site.register(ItemLoanPayment)
admin.site.register(CustomerItemLoan)
admin.site.register(MoneyLoanPayment)
admin.site.register(CustomerMoneyLoan)