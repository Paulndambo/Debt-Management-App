from django.urls import path
from core.views import home, items, NewInventoryItemView, restock

urlpatterns = [
    path("", home, name="home"),
    path("items/", items, name="items"),
    path("new-item/", NewInventoryItemView.as_view(), name="new-item"),
    path("restock/<int:item_pk>/", restock, name="restock"),
]