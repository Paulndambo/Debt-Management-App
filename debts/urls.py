from django.urls import path

from debts.views import (
    loans, customer_item_loans, customer_money_loans, borrowed_items,
    money_loan_payments, item_loan_payments, loan_applications, customer_money_loan_detail,
    customer_item_loan_detail, pay_money_loan, pay_item_loan, resubmit_loan_application,
    decline_loan_application, approve_loan_application, disburse_loan_application, LoanApplyView
)

urlpatterns = [
    path("loans/", loans, name="loans"),
    
    
    path("borrowed-items/", borrowed_items, name="borrowed-items"),

    path("money-loans/", customer_money_loans, name="money-loans"),
    path("money-loans/<int:customer_id>/", customer_money_loans, name="money-loans"),
    path("money-loan-payments/", money_loan_payments, name="money-loan-payments"),
    path("money-loan-payments/<int:loan_id>/", money_loan_payments, name="money-loan-payments"),
    path("money-loan-detail/<int:loan_id>/", customer_money_loan_detail, name="money-loan-detail"),
    path("pay-money-loan/<int:customer_id>/<int:loan_id>/", pay_money_loan, name="pay-money-loan"),
    path("disburse-loan/<int:pk>/", disburse_loan_application, name="disburse-loan"),
    

    path("item-loans/", customer_item_loans, name="item-loans"),
    path("item-loans/<int:customer_id>/", customer_item_loans, name="item-loans"),
    path("item-loan-payments/", item_loan_payments, name="item-loan-payments"),
    path("item-loan-payments/<int:loan_id>/", item_loan_payments, name="item-loan-payments"),
    path("item-loan-detail/<int:loan_id>/", customer_item_loan_detail, name="item-loan-detail"),
    path("pay-item-loan/<int:customer_id>/<int:loan_id>/", pay_item_loan, name="pay-item-loan"),


    path("loan-applications/", loan_applications, name="loan-applications"),
    path("resubmit-loan-application/<int:pk>/", resubmit_loan_application, name="resubmit-loan-application"),
    path("decline-loan-application/<int:pk>/", decline_loan_application, name="decline-loan-application"),
    path("approve-loan-application/<int:pk>/", approve_loan_application, name="approve-loan-application"),
    path("apply-loan/", LoanApplyView.as_view(), name="apply-loan"),
]