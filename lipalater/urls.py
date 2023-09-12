from django.urls import path
from lipalater.views import lipalater_loans, premiums, new_lipa_later_loan


urlpatterns = [
    path("", lipalater_loans, name="lipa-polepole-loans"),
    path("premiums/", premiums, name="premiums"),
    path("new-gas-loan/", new_lipa_later_loan, name="new-gas-loan"),
]