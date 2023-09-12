from django.urls import path

from users.views import (
    user_login, customers, NewCustomerView, customer_detail, UpdateCustomerView, users
)
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("users/", users, name="users"),
    path("customers/", customers, name="customers"),
    path("new-customer/", NewCustomerView.as_view(), name="new-customer"),
    path("customer/<int:pk>/edit/", UpdateCustomerView.as_view(), name="update-customer"),
    path("customers/<int:pk>/", customer_detail, name="customer-detail"),
]