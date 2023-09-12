from django.urls import path
from lipalater.views import lipalater_loans, premiums, NewLipaLateLoanView


urlpatterns = [
    path("", lipalater_loans, name="lipa-polepole-loans"),
    path("premiums/", premiums, name="premiums"),
    path("new-gas-loan/", NewLipaLateLoanView.as_view(), name="new-gas-loan"),
]