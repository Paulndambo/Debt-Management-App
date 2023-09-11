from django.shortcuts import render

from lipalater.models import LipaLaterLoan, LipaLaterLoanPremium, MpesaTransaction
# Create your views here.
def lipalater_loans(request):
    loans = LipaLaterLoan.objects.all()
    context = {
        "loans": loans
    }
    return render(request, "lipalater/lipalater_loans.html", context)