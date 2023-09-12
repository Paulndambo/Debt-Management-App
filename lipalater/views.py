from django.shortcuts import render

from lipalater.models import LipaLaterLoan, LipaLaterLoanPremium, MpesaTransaction
from users.models import Customer
# Create your views here.
def lipalater_loans(request):
    loans = LipaLaterLoan.objects.all()
    context = {
        "loans": loans
    }
    return render(request, "lipalater/lipalater_loans.html", context)

def new_lipa_later_loan(request, customer_id=None):
    customer = Customer.objects.get(id=customer)

    if request.method == "POST":
        pass

    context = {
        "customer": customer
    }
        
    return render(request, "lipalater/new_loan.html", context)


def premiums(request):
    premiums = LipaLaterLoanPremium.objects.all().order_by("-created")
    context = {
        "premiums": premiums
    }
    return render(request, "lipalater/premiums/premiums.html", context)


def new_premium(request):
    return render(request, "lipalater/premiums/new_premium.html")