from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, CreateView, DeleteView
from decimal import Decimal

from .models import Inventory
from .forms import InventoryForm

# Create your views here.
@login_required(login_url="/accounts/login/")
def home(request):
    return render(request, "index.html")


def items(request):
    items = Inventory.objects.all().order_by("-created")
    context = {
        "items": items
    }
    return render(request, "inventory/items.html", context)


class NewInventoryItemView(CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = "inventory/new_item.html"


def restock(request, item_pk=None):
    inventory = Inventory.objects.get(id=item_pk)

    if request.method == "POST":
        amount = Decimal(request.POST.get("amount"))

        inventory.stock += amount
        print(f"Restock Amount: {amount}, Original Amt: {inventory.stock}")
        inventory.save()
        return redirect(reverse("items"))

    return render(request, "inventory/restock.html", {"inventory": inventory})