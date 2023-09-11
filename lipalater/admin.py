from django.contrib import admin
from lipalater.models import LipaLaterLoan, LipaLaterLoanPremium, MpesaTransaction

# Register your models here.
@admin.register(LipaLaterLoan)
class LipaLaterLoanAdmin(admin.ModelAdmin):
    list_display = ["customer", "item", "expected_amount", "amount_paid", "status"]