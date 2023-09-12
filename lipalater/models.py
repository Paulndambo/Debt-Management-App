from django.db import models
from core.models import AbstractBaseModel
from django.urls import reverse
from core.constants import LOAN_STATUS_CHOICES
# Create your models here.
PREMIUM_STATUS_CHOICES = (
    ("unpaid", "Unpaid"),
    ("pending", "Pending"),
    ("paid", "Paid"),
    ("paying", "Paying"),
    ("reviewing", "Reviewing"),
)

class LipaLaterLoan(AbstractBaseModel):
    customer = models.ForeignKey("users.Customer", on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey("core.Inventory", on_delete=models.SET_NULL, null=True)
    expected_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=255, choices=LOAN_STATUS_CHOICES)

    #def __str__(self):
    #    return self.item.name

    def get_absolute_url(self):
        return reverse("lipa-polepole-loans")


class LipaLaterLoanPremium(AbstractBaseModel):
    loan = models.ForeignKey(LipaLaterLoan, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expected_date = models.DateField()
    status = models.CharField(max_length=255, choices=PREMIUM_STATUS_CHOICES)

    def __str__(self):
        return self.status


class MpesaTransaction(AbstractBaseModel):
    phone_number = models.CharField(max_length=255)
    payment_date = models.DateField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.phone_number