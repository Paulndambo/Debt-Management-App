from django.shortcuts import render
from django.views.generic import CreateView
from lipalater.models import LipaLaterLoan, LipaLaterLoanPremium, MpesaTransaction
from users.models import Customer
from lipalater.forms import LipaLaterLoanForm
# Create your views here.
def lipalater_loans(request):
    loans = LipaLaterLoan.objects.all()
    context = {
        "loans": loans
    }
    return render(request, "lipalater/lipalater_loans.html", context)

class NewLipaLateLoanView(CreateView):
    model = LipaLaterLoan
    form_class = LipaLaterLoanForm
    template_name = "lipalater/new_loan.html"

    def post(self, request, *args, **kwargs):
        
        customer = request.POST.get("customer")
        item = request.POST.get("item")

        print(f"Customer: {customer}, Item: {item}")
        
        return super().post(request, *args, **kwargs)


def premiums(request):
    premiums = LipaLaterLoanPremium.objects.all().order_by("-created")
    context = {
        "premiums": premiums
    }
    return render(request, "lipalater/premiums/premiums.html", context)


def new_premium(request):
    return render(request, "lipalater/premiums/new_premium.html")