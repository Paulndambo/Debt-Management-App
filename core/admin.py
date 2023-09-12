from django.contrib import admin
from .models import Inventory
# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ["name", "unit_price", "selling_price", "unit", "installment_amount", "stock"]