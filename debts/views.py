from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from decimal import Decimal
from debts.models import (
    CustomerItemLoan, CustomerMoneyLoan, ItemBorrowed, 
    MoneyLoanPayment, ItemLoanPayment, LoanApplication
)

from .forms import MoneyLoanPaymentForm
from users.models import Customer

# Create your views here.
def loans(request):
    return render(request, "loans/loans.html")


def loan_applications(request):
    loan_applications = LoanApplication.objects.all().order_by("-created")
    context = {
        "loan_applications": loan_applications
    }
    return render(request, "loans/loan_applications.html", context)


def resubmit_loan_application(request, pk):
    loan_application = LoanApplication.objects.get(id=pk)
    loan_application.status = "Pending"
    loan_application.save()
    return redirect("loan-applications")


def approve_loan_application(request, pk):
    loan_application = LoanApplication.objects.get(id=pk)
    loan_application.status = "Approved"
    loan_application.save()
    return redirect("loan-applications")


def decline_loan_application(request, pk):
    loan_application = LoanApplication.objects.get(id=pk)
    loan_application.status = "Declined"
    loan_application.save()
    return redirect("loan-applications")


def customer_item_loans(request, customer_id=None):
    item_loans = CustomerItemLoan.objects.all().order_by("-created")

    if customer_id:
        item_loans = CustomerItemLoan.objects.filter(customer__id=customer_id).order_by("-created")

    context = {
        "item_loans": item_loans
    }
    return render(request, "loans/item_loans.html", context)


def item_loan_payments(request, loan_id=None):
    items_loan_payments = ItemLoanPayment.objects.all().order_by("-created")

    customer_id = None

    if loan_id:
        items_loan_payments = ItemLoanPayment.objects.filter(loan__id=loan_id).order_by("-created")

        loan = CustomerItemLoan.objects.get(id=loan_id)
        customer_id = loan.customer.id

    context = {
        "loan_payments": items_loan_payments,
        "loan_id": loan_id,
        "customer_id": customer_id
    }
    return render(request, "loans/items_loan_payments.html", context)


def customer_item_loan_detail(request, loan_id=None):
    loan = CustomerItemLoan.objects.get(id=loan_id)

    if loan_id:
        item_loan_payments = ItemLoanPayment.objects.filter(loan__id=loan_id).order_by("-created")

    context = {
        "loan": loan,
        "loan_payments": item_loan_payments
    }
    return render(request, "loans/item_loan.html", context)



def pay_item_loan(request, customer_id=None, loan_id=None):
    customer = Customer.objects.get(id=customer_id)
    loan = CustomerItemLoan.objects.get(id=loan_id)

    name = f"{customer.first_name} {customer.last_name}"
    
    if request.method == "POST":
        amount = request.POST.get("amount")
        payment = ItemLoanPayment(loan=loan, customer=customer, amount=amount)
        payment.save()

        loan.amount_repaid += Decimal(amount)
        loan.save()

        return redirect(reverse("item-loan-detail", kwargs={"loan_id": loan_id}))
        
    context = {
        "name": name,
        "loan": loan
    }

    
    return render(request, "loans/payments/pay_item_loan.html", context)



def borrowed_items(request):
    borrowed_items = ItemBorrowed.objects.all().order_by("-created")
    context = {
        "borrowed_items": borrowed_items
    }
    return render(request, "loans/borrowed_items.html", context)


def customer_money_loans(request, customer_id=None):
    money_loans = CustomerMoneyLoan.objects.all().order_by("-created")

    if customer_id:
        money_loans = CustomerMoneyLoan.objects.filter(customer__id=customer_id).order_by("-created")

    context = {
        "money_loans": money_loans
    }
    return render(request, "loans/money_loans.html", context)


def customer_money_loan_detail(request, loan_id=None):
    loan = CustomerMoneyLoan.objects.get(id=loan_id)

    if loan_id:
        money_loan_payments = MoneyLoanPayment.objects.filter(loan__id=loan_id).order_by("-created")

    context = {
        "loan": loan,
        "loan_payments": money_loan_payments
    }
    return render(request, "loans/money_loan.html", context)



def money_loan_payments(request, loan_id=None):
    money_loan_payments = MoneyLoanPayment.objects.all().order_by("-created")

    customer_id = None

    if loan_id:
        money_loan_payments = MoneyLoanPayment.objects.filter(loan__id=loan_id).order_by("-created")

        loan = CustomerMoneyLoan.objects.get(id=loan_id)
        customer_id = loan.customer.id


    context = {
        "loan_payments": money_loan_payments,
        "loan_id": loan_id,
        "customer_id": customer_id
    }
    return render(request, "loans/money_loan_payments.html", context)


def pay_money_loan(request, customer_id=None, loan_id=None):

    customer = Customer.objects.get(id=customer_id)
    loan = CustomerMoneyLoan.objects.get(id=loan_id)

    name = f"{customer.first_name} {customer.last_name}"
    
    if request.method == "POST":
        amount = request.POST.get("amount")
        payment = MoneyLoanPayment(loan=loan, customer=customer, amount=amount)
        payment.save()

        loan.amount_repaid += Decimal(amount)
        loan.save()

        return redirect(reverse("money-loan-detail", kwargs={"loan_id": loan_id}))
        

    context = {
        "name": name,
        "loan": loan
    }

    
    return render(request, "loans/payments/pay_money_loan.html", context)