from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import UpdateView, CreateView, DeleteView
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.db.models import Q
from .forms import LoginForm, CustomerForm
from django.contrib import messages
from users.models import Customer

from django.contrib.auth.decorators import login_required


def user_login(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.error(request, "Invalid Credentials, Try Again")
        else:
            messages.error(request, "Error Valid Details, Try Again")

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


@login_required(login_url="/accounts/login/")
def customers(request):
    customers = Customer.objects.all()

    if request.method == "POST":
        id_number = request.POST.get("id_number")

        if id_number:
            customers = customers.filter(id_number=id_number)

    context = {
        "customers": customers
    }
    return render(request, "customers/customers.html", context)


def customer_detail(request, pk=None):
    customer = Customer.objects.get(id=pk)
    money_loans = customer.moneyloans.all().order_by("-created")
    item_loans = customer.itemloans.all().order_by("-created")
    context = {
        "customer": customer,
        "money_loans": money_loans,
        "item_loans": item_loans
    }
    return render(request, "customers/customer.html", context)


class NewCustomerView(CreateView):
    model = Customer
    form_class = CustomerForm
    # fields = "__all__"
    template_name = "customers/new_customer.html"


class UpdateCustomerView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/update_customer.html"


def users(request):
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, "accounts/users.html", context)
