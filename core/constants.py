MONTHS_LIST = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)

LOAN_STATUS_CHOICES = (
    ("Paid", "Paid"),
    ("Defaulted", "Defaulted"),
    ("Paying", "Paying"),
    ("Reviewing", "Reviewing"),
)

def get_loan_status(amount_borrowed, amount_paid):
    loan_status = ''
    if amount_borrowed == amount_paid:
        loan_status = 'Paid'
    elif amount_borrowed > amount_paid:
        loan_status = 'Paying'

    return loan_status