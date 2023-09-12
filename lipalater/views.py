from django.shortcuts import render, redirect
from django.views.generic import CreateView
from lipalater.models import LipaLaterLoan, LipaLaterLoanPremium, MpesaTransaction
from users.models import Customer
from core.models import Inventory
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
        
        customer_id = int(request.POST.get("customer"))
        item_id = int(request.POST.get("item"))

        item = Inventory.objects.get(id=item_id)

        loan = LipaLaterLoan.objects.create(
            customer_id=customer_id,
            item=item,
            expected_amount=item.selling_price,
            amount_paid=0,
            status="pending"
        )


        print(f"Customer: {customer_id}, Item: {item.name}")
        
        return redirect("lipa-polepole-loans")


def premiums(request):
    premiums = LipaLaterLoanPremium.objects.all().order_by("-created")
    context = {
        "premiums": premiums
    }
    return render(request, "lipalater/premiums/premiums.html", context)


def new_premium(request):
    return render(request, "lipalater/premiums/new_premium.html")