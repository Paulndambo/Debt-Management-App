from django.db import models
from core.models import AbstractBaseModel
from core.constants import MONTHS_LIST, LOAN_STATUS_CHOICES, get_loan_status, YEARS_CHOICE_LIST
from django.urls import reverse

# Create your models here.
LOAN_APPLICATION_STATUS = (
    ("Approved", "Approved"),
    ("Declined", "Declined"),
    ("Pending", "Pending"),
)


class LoanApplication(AbstractBaseModel):
    customer = models.ForeignKey("users.Customer", on_delete=models.CASCADE, related_name="loanapplications")
    amount_applied = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=255, choices=LOAN_APPLICATION_STATUS, default="Pending")
    disburse = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("loan-applications")


class CustomerItemLoan(AbstractBaseModel):
    customer = models.ForeignKey("users.Customer", on_delete=models.CASCADE, related_name="itemloans")
    amount_borrowed = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount_repaid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=255, choices=LOAN_STATUS_CHOICES, null=True)


    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name}"

    def current_year(self):
        return self.created.date().year

    def balance(self):
        return self.amount_borrowed - self.amount_repaid


class ItemBorrowed(AbstractBaseModel):
    customer = models.ForeignKey("users.Customer", on_delete=models.CASCADE, related_name="itemsborrowed")
    item = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    month = models.CharField(max_length=255, null=True)
    year = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name}"


class CustomerMoneyLoan(AbstractBaseModel):
    customer = models.ForeignKey("users.Customer", on_delete=models.CASCADE, related_name="moneyloans")
    amount_awarded = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount_repaid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_awarded = models.DateField()
    expected_repay_date = models.DateField(null=True)
    status = models.CharField(max_length=255, choices=LOAN_STATUS_CHOICES, default="Paying")
    interest_accrued = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name}"


    def amount_to_repay(self):
        return self.amount_awarded + self.interest_accrued




class MoneyLoanPayment(AbstractBaseModel):
    loan = models.ForeignKey(CustomerMoneyLoan, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey("users.Customer", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name}"




class ItemLoanPayment(AbstractBaseModel):
    loan = models.ForeignKey(CustomerItemLoan, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey("users.Customer", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name}"
    